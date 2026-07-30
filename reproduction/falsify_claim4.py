from __future__ import annotations

import math
from fractions import Fraction


def ceiling_scale(constant: float, base: float) -> int:
    return max(1, math.ceil(constant * base))


def build_instance(constants: dict, delta: Fraction, s: int) -> dict:
    sample_constant = float(constants["sample"])
    restart_constant = float(constants["restarts"])
    iteration_constant = float(constants["iterations"])
    r = ceiling_scale(restart_constant, s * s)
    d = max(2 * r + 1, math.ceil(4 / float(delta)))
    sample_base = s * s * math.log(s) * math.log(d / float(delta))
    n = ceiling_scale(sample_constant, sample_base)
    iterations = ceiling_scale(iteration_constant, math.log(s))

    nuisance_ratio = Fraction(9, 10)
    weighted_coordinates = 1 + nuisance_ratio * (d - 1)
    total_nonzero = delta / (4 * n)
    top_atom_probability = total_nonzero / weighted_coordinates
    all_zero_lower = 1 - n * total_nonzero
    conditional_success_upper = Fraction(1, d)
    success_upper = 1 - all_zero_lower + conditional_success_upper

    return {
        "hidden_constants": constants,
        "s": s,
        "d": d,
        "n": n,
        "r": r,
        "iterations": iterations,
        "sample_scale_without_hidden_constant": sample_base,
        "distribution": {
            "support": "0 and signed standard basis vectors",
            "top_atom_probability_each_sign": str(top_atom_probability / 2),
            "nuisance_atom_probability_each_sign": str(
                nuisance_ratio * top_atom_probability / 2
            ),
            "zero_probability": str(1 - total_nonzero),
            "total_nonzero_probability": str(total_nonzero),
        },
        "model_audit": {
            "mean_zero": True,
            "positive_semidefinite_covariance": True,
            "lambda1": str(top_atom_probability),
            "lambda2": str(nuisance_ratio * top_atom_probability),
            "lambda2_over_lambda1": "9/10",
            "top_eigenvector": "e_j",
            "top_eigenvector_nnz": 1,
            "sparsity_budget": s,
            "bounded_norm": 1,
            "one_subgaussian_certificate": (
                "For every unit u, <u,X> is mean-zero in "
                "[-||u||_infinity,||u||_infinity]; Hoeffding's lemma gives "
                "E exp(t<u,X>) <= exp(t^2||u||_infinity^2/2) "
                "<= exp(t^2||u||_2^2/2)."
            ),
        },
        "proof": {
            "all_zero_probability_lower": str(all_zero_lower),
            "all_zero_probability_lower_decimal": float(all_zero_lower),
            "nonzero_event_probability_upper": str(1 - all_zero_lower),
            "conditional_success_upper_for_some_j": str(conditional_success_upper),
            "unconditional_success_upper": str(success_upper),
            "unconditional_success_upper_decimal": float(success_upper),
            "required_success_lower": str(1 - delta),
            "required_success_lower_decimal": float(1 - delta),
            "reason": (
                "On the all-zero dataset every j produces identical observations. "
                "A unit output has squared correlation at least 0.9 with at most "
                "one of e_1,...,e_d, so averaging over j gives a hard instance "
                "with conditional success at most 1/d."
            ),
        },
        "formal_theorem_scope": {
            "sigma": 1,
            "omitted_factor": "(sigma^2/lambda1)^2",
            "omitted_factor_lower_bound": str(1 / (top_atom_probability**2)),
            "formal_theorem_2_contradicted": False,
        },
    }


def run(config: dict, seed: int) -> dict:
    delta = Fraction(config["delta_numerator"], config["delta_denominator"])
    instances = [
        build_instance(constants, delta, int(config["s"]))
        for constants in config["hidden_constant_audit"]
    ]
    return {
        "status": "FALSIFIED",
        "seed": seed,
        "seed_role": "Recorded for reproducibility; the proof certificate is deterministic.",
        "paper_statement_under_test": (
            "Informal Theorem 1: under Model 2, RTPM succeeds with squared "
            "correlation at least 0.9 and probability at least 1-delta using "
            "n=Omega(s^2 log(s) log(d/delta)), r=Omega(s^2), and T=Omega(log(s))."
        ),
        "quantifier_certificate": {
            "scope": "every finite positive choice of the three hidden constants",
            "construction": (
                "After the constants fix n,r,T, choose a bounded Model-2 "
                "distribution whose total nonzero mass is delta/(4n)."
            ),
            "why_finite_instances_are_not_the_proof": (
                "The algebraic construction and inequalities are parameterized "
                "by arbitrary constants; listed instances are machine-checkable "
                "sanity checks."
            ),
        },
        "delta": str(delta),
        "instances": instances,
        "algorithm_behavior": {
            "literal_algorithm_1": (
                "On an all-zero first block, Top_r(0)/||Top_r(0)|| divides by zero."
            ),
            "defensive_fallback_covered": True,
            "reason": (
                "The indistinguishability bound applies to any deterministic or "
                "randomized fallback that depends only on the observed data."
            ),
        },
        "limitations": [
            "This falsifies the scale-free informal Theorem 1 statement and the imported Claim 4 contract.",
            "It does not contradict formal Theorem 2, whose sample bound contains (sigma^2/lambda1)^2.",
            "It does not assess whether RTPM works after adding a lower signal-scale assumption.",
        ],
    }
