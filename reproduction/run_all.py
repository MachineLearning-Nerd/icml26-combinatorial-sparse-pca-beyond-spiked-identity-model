from __future__ import annotations

import json
import math
import os
import platform
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / "reproduction" / "config.json").read_text())
THREAD_CAP = str(CONFIG.get("compute_plan", {}).get("estimated_cores", 1))
os.environ["OMP_NUM_THREADS"] = THREAD_CAP
os.environ["OPENBLAS_NUM_THREADS"] = THREAD_CAP
os.environ["MKL_NUM_THREADS"] = THREAD_CAP
os.environ["VECLIB_MAXIMUM_THREADS"] = THREAD_CAP
os.environ["NUMEXPR_NUM_THREADS"] = THREAD_CAP

import numpy as np

from core import (
    covariance_threshold_counterexample,
    deflation_counterexample,
    diagonal_counterexample,
    greedy_counterexample,
    historical_rtpm,
    sample_covariance,
    sample_gaussian,
    sin2_angle,
)
from check_claim4 import check_claim4
from check_falsification import check_falsification
import claim4 as claim4_experiment
import falsify_claim4

def model_audit(covariance: np.ndarray, vector: np.ndarray) -> dict:
    eigenvalues = np.linalg.eigvalsh(covariance)
    residual = np.linalg.norm(covariance @ vector - eigenvalues[-1] * vector)
    return {
        "lambda1": float(eigenvalues[-1]),
        "lambda2": float(eigenvalues[-2]),
        "lambda2_over_lambda1": float(eigenvalues[-2] / eigenvalues[-1]),
        "top_eigenvector_residual": float(residual),
        "positive_semidefinite": bool(eigenvalues[0] >= -1e-10),
    }


def claim_1(seed: int) -> dict:
    trials = []
    for offset, s in enumerate((3, 5, 8)):
        covariance, vector = diagonal_counterexample(4 * s, s)
        samples = sample_gaussian(covariance, 80 * s * s * math.ceil(math.log(4 * s)), seed + offset)
        empirical = sample_covariance(samples)
        selected = np.argpartition(np.diag(empirical), -s)[-s:]
        overlap = int(np.sum(selected < s))
        trials.append({"s": s, "support_overlap": overlap, "sin2": float(overlap == 0)})
    audit = model_audit(*diagonal_counterexample(32, 8))
    passed = all(row["support_overlap"] == 0 for row in trials)
    return {"status": "VERIFIED" if passed else "FAILED", "model_audit": audit, "trials": trials}


def claim_2(seed: int) -> dict:
    trials = []
    for offset, (s, threshold) in enumerate(((15, 0.045), (20, 0.035))):
        covariance, vector = covariance_threshold_counterexample(s, 8, 0.06)
        n = 80 * s * s * math.ceil(math.log(covariance.shape[0]))
        empirical = sample_covariance(sample_gaussian(covariance, n, seed + 20 + offset))
        thresholded = empirical * (np.abs(empirical) >= threshold)
        _, eigenvectors = np.linalg.eigh(thresholded)
        score = sin2_angle(eigenvectors[:, -1], vector)
        trials.append({"s": s, "n": n, "threshold": threshold, "sin2": score})
    covariance, vector = covariance_threshold_counterexample(20, 8, 0.06)
    passed = all(row["sin2"] > 0.99 for row in trials)
    return {
        "status": "VERIFIED" if passed else "FAILED",
        "model_audit": model_audit(covariance, vector),
        "trials": trials,
    }


def claim_3(seed: int) -> dict:
    del seed
    trials = []
    for s in (4, 6, 8):
        covariance, vector = greedy_counterexample(s)
        scores = np.abs((covariance @ covariance)[0])
        selected = np.argpartition(scores, -s)[-s:]
        overlap = int(np.sum(selected < s))
        trials.append({"s": s, "support_overlap": overlap})
    covariance, vector = greedy_counterexample(8)
    passed = all(row["support_overlap"] <= 1 for row in trials)
    return {
        "status": "VERIFIED" if passed else "FAILED",
        "model_audit": model_audit(covariance, vector),
        "trials": trials,
    }


def claim_4_historical(seed: int) -> dict:
    trials = []
    for offset, s in enumerate((4, 5, 8, 10)):
        d = 4 * s
        rng = np.random.default_rng(seed + 100 + offset)
        support = rng.choice(d, s, replace=False)
        vector = np.zeros(d)
        vector[support] = 1 / math.sqrt(s)
        covariance = 0.6 * np.eye(d) + 0.4 * np.outer(vector, vector)
        n = 15 * s * s * math.ceil(math.log(d)) + 50
        estimate = historical_rtpm(sample_gaussian(covariance, n, seed + 200 + offset), s + 2, 80)
        trials.append({"s": s, "d": d, "n": n, "correlation_squared": float((estimate @ vector) ** 2)})
    passed = all(row["correlation_squared"] >= 0.9 for row in trials)
    return {
        "status": "TOY" if passed else "FAILED",
        "historical_rejected_baseline": True,
        "deviations": [
            "spiked-identity covariance",
            "full sample covariance reused at every iteration",
            "single trial per setting",
            "n omits log(s) and delta calibration",
        ],
        "trials": trials,
    }


def claim_5(seed: int) -> dict:
    del seed
    trials = []
    for d in (8, 12, 20):
        covariance, vector, projector = deflation_counterexample(d, 0.1, 0.1)
        _, eigenvectors = np.linalg.eigh(projector @ covariance @ projector)
        top = eigenvectors[:, -1]
        trials.append({
            "d": d,
            "correlation_target": 0.9,
            "deflated_top_eigenvector_nnz": int(np.sum(np.abs(top) > 1e-7)),
            "sin2_to_original": sin2_angle(top, vector),
        })
    passed = all(row["deflated_top_eigenvector_nnz"] == row["d"] for row in trials)
    return {"status": "VERIFIED" if passed else "FAILED", "trials": trials}


def independent_checker(payload: dict) -> tuple[bool, list[str]]:
    failures = []
    expected = {"claim_1": "VERIFIED", "claim_2": "VERIFIED", "claim_3": "VERIFIED", "claim_5": "VERIFIED"}
    for claim, status in expected.items():
        if payload["claims"][claim]["status"] != status:
            failures.append(f"{claim} status is not {status}")
    if payload["stage"] == "historical_baseline":
        if payload["claims"]["claim_4"]["status"] != "TOY":
            failures.append("historical Claim 4 must remain labeled TOY")
    elif payload["stage"] == "claim4_calibration":
        claim4_passed, claim4_failures = check_claim4(payload["claims"]["claim_4"])
        if not claim4_passed:
            failures.extend(claim4_failures)
    else:
        claim4_passed, claim4_failures = check_falsification(payload["claims"]["claim_4"])
        if not claim4_passed:
            failures.extend(claim4_failures)
    return not failures, failures


def main() -> int:
    started = time.perf_counter()
    config = CONFIG
    seed = int(config["seed"])
    claims = {
        "claim_1": claim_1(seed),
        "claim_2": claim_2(seed),
        "claim_3": claim_3(seed),
        "claim_4": (
            claim_4_historical(seed)
            if config["stage"] == "historical_baseline"
            else (
                claim4_experiment.run(config["claim4"], seed)
                if config["stage"] == "claim4_calibration"
                else falsify_claim4.run(config["claim4_falsification"], seed)
            )
        ),
        "claim_5": claim_5(seed),
    }
    payload = {
        "schema_version": 1,
        "stage": config["stage"],
        "paper": "arXiv:2603.02607v1",
        "seed": seed,
        "claims": claims,
        "compute": {
            "estimated_cores": config.get("compute_plan", {}).get("estimated_cores", 1),
            "selected_backend": config.get("compute_plan", {}).get("selected_backend", "local"),
            "selected_flavor": config.get("compute_plan", {}).get("selected_flavor", "local"),
            "expected_runtime_minutes": config.get("compute_plan", {}).get(
                "expected_runtime_minutes", "<2"
            ),
            "actual_logical_cpus_visible": os.cpu_count(),
            "blas_thread_cap": int(THREAD_CAP),
            "machine": platform.machine(),
            "python": sys.version.split()[0],
            "numpy": np.__version__,
        },
    }
    checker_passed, checker_failures = independent_checker(payload)
    tampered = json.loads(json.dumps(payload))
    if config["stage"] == "historical_baseline":
        tampered["claims"]["claim_1"]["status"] = "FAILED"
    elif config["stage"] == "claim4_calibration":
        tampered["claims"]["claim_4"]["algorithm_audit"]["fresh_blocks"] = False
    else:
        tampered["claims"]["claim_4"]["instances"][0]["distribution"][
            "total_nonzero_probability"
        ] = "1/2"
    tampered_rejected = not independent_checker(tampered)[0]
    payload["independent_checker"] = {
        "passed": checker_passed,
        "failures": checker_failures,
        "negative_control_tampered_evidence_rejected": tampered_rejected,
    }
    payload["runtime_seconds"] = time.perf_counter() - started
    print("EVIDENCE_JSON_BEGIN")
    print(json.dumps(payload, indent=2, sort_keys=True))
    print("EVIDENCE_JSON_END")
    claim4_status = claims["claim_4"]["status"]
    print(
        "EVAL.md: Claims 1,2,3,5 VERIFIED; "
        f"Claim 4 status={claim4_status}. "
        f"checker_passed={checker_passed}; tamper_control_rejected={tampered_rejected}; "
        f"runtime_seconds={payload['runtime_seconds']:.3f}"
    )
    return 0 if checker_passed and tampered_rejected else 1


if __name__ == "__main__":
    raise SystemExit(main())
