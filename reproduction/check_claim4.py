from __future__ import annotations


def check_claim4(evidence: dict) -> tuple[bool, list[str]]:
    failures = []
    algorithm = evidence["algorithm_audit"]
    for key in (
        "fresh_blocks",
        "all_d_standard_basis_restarts",
        "top_r_each_iteration",
        "empirical_rayleigh_selection",
    ):
        if not algorithm.get(key):
            failures.append(f"algorithm audit failed: {key}")
    if algorithm.get("sample_threshold_selected_from_theorem_formula"):
        failures.append("sample threshold selection is circular")
    for setting in evidence["settings"]:
        label = f"s={setting['s']},d={setting['d']}"
        audit = setting["model_audit"]
        if not audit["positive_semidefinite"]:
            failures.append(f"{label}: covariance is not PSD")
        if audit["lambda2_over_lambda1"] > 0.9 + 1e-9:
            failures.append(f"{label}: eigengap violates Model 2")
        if audit["top_eigenvector_residual"] > 1e-8:
            failures.append(f"{label}: supplied sparse vector is not top eigenvector")
        if audit["vector_nnz"] > audit["s"]:
            failures.append(f"{label}: top eigenvector is not s-sparse")
        if not audit["non_spherical"]:
            failures.append(f"{label}: covariance is a spherical/spiked-identity proxy")
        confirmation = setting["confirmation"]
        if confirmation["wilson_95_lower"] < 0.9:
            failures.append(f"{label}: 95% lower confidence bound is below 0.9")
        if not confirmation["all_negative_controls_failed_as_intended"]:
            failures.append(f"{label}: a negative control unexpectedly recovered")
        if not setting["operation_count_audit"]["block_size_at_least_d"]:
            failures.append(f"{label}: T*d^3 is not absorbed by n*d^2")
    return not failures, failures

