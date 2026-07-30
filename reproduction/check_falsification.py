from __future__ import annotations

from fractions import Fraction


def check_falsification(evidence: dict) -> tuple[bool, list[str]]:
    failures = []
    if evidence.get("status") != "FALSIFIED":
        failures.append("Claim 4 status is not FALSIFIED")
    if evidence.get("algorithm_behavior", {}).get("defensive_fallback_covered") is not True:
        failures.append("defensive fallbacks are not covered")
    for index, instance in enumerate(evidence.get("instances", [])):
        label = f"instance {index}"
        audit = instance["model_audit"]
        if not audit["mean_zero"]:
            failures.append(f"{label}: distribution is not mean zero")
        if not audit["positive_semidefinite_covariance"]:
            failures.append(f"{label}: covariance is not PSD")
        if Fraction(audit["lambda2_over_lambda1"]) > Fraction(9, 10):
            failures.append(f"{label}: eigengap violates Model 2")
        if audit["top_eigenvector_nnz"] > audit["sparsity_budget"]:
            failures.append(f"{label}: top eigenvector violates sparsity")
        if audit["bounded_norm"] > 1:
            failures.append(f"{label}: boundedness certificate exceeds 1")

        n = int(instance["n"])
        d = int(instance["d"])
        delta = Fraction(evidence["delta"])
        total_nonzero = Fraction(instance["distribution"]["total_nonzero_probability"])
        expected_total_nonzero = delta / (4 * n)
        if total_nonzero != expected_total_nonzero:
            failures.append(f"{label}: rare-event mass is not delta/(4n)")
        all_zero_lower = Fraction(instance["proof"]["all_zero_probability_lower"])
        if all_zero_lower != 1 - n * total_nonzero:
            failures.append(f"{label}: union-bound certificate is inconsistent")
        conditional_upper = Fraction(
            instance["proof"]["conditional_success_upper_for_some_j"]
        )
        if conditional_upper != Fraction(1, d):
            failures.append(f"{label}: indistinguishability bound is not 1/d")
        success_upper = Fraction(instance["proof"]["unconditional_success_upper"])
        if success_upper != n * total_nonzero + Fraction(1, d):
            failures.append(f"{label}: success upper bound is inconsistent")
        if Fraction(1, d) > delta / 4:
            failures.append(f"{label}: d is too small for the advertised bound")
        if success_upper > delta / 2:
            failures.append(f"{label}: success upper bound exceeds delta/2")
        if success_upper >= 1 - delta:
            failures.append(f"{label}: certificate does not contradict the target")
        if instance["r"] > d:
            failures.append(f"{label}: restart sparsity r exceeds d")
        if instance["formal_theorem_scope"]["formal_theorem_2_contradicted"]:
            failures.append(f"{label}: evidence incorrectly claims to refute Theorem 2")
    if not evidence.get("instances"):
        failures.append("no numeric sanity instances")
    return not failures, failures
