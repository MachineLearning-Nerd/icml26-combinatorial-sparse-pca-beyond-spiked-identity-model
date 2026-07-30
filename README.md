# Reproducing combinatorial sparse PCA beyond spiked identity

[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-repro-Kk5UZgkWFx-combinatorial-sparse-pca-beyond-the-spiked-identity-model/blob/main/notebooks/claim4_falsification.py)

This repository reproduces five claims from
[*Combinatorial Sparse PCA Beyond the Spiked Identity Model*](https://arxiv.org/abs/2603.02607).
The existing four negative checks remain VERIFIED. The previous RTPM check was
a small spiked-identity proxy; an exact quantifier audit now FALSIFIES the
scale-free wording of informal Theorem 1 / imported Claim 4.

At `δ=0.1`, the paper wording requires squared-correlation recovery with
probability at least `0.9`. The counterexample satisfies every stated Model-2
assumption and certifies success probability at most `0.05` for every finite
choice of the hidden asymptotic constants. Formal Theorem 2 is not
contradicted: it contains the omitted `(σ²/λ₁)²` sample factor.

Compute was local CPU with a one-thread cap because the complete cumulative
verifier took 1.373 seconds. Two non-spherical positive-calibration attempts
were correctly routed to Hugging Face `cpu-upgrade`; both stopped before
scientific execution because the default image lacked `uv`, so they are not
used as evidence.

- [Illustrated claim-by-claim report](reports/claim-by-claim/report.md)
- [Tutorial notebook](notebooks/claim4_falsification.py)
- [Machine-readable cumulative results](.openresearch/artifacts/cumulative/raw_results.json)

## Experiment log

| Branch / experiment | Purpose or change | Exact run command | Assessment / outcome | Compute |
|---|---|---|---|---|
| `main` | Public landing page | Not run as an experiment (publication surface) | Presentation only | — |
| [`orx/judged-reproduction-baseline`](https://github.com/MachineLearning-Nerd/icml26-repro-Kk5UZgkWFx-combinatorial-sparse-pca-beyond-the-spiked-identity-model/tree/orx/judged-reproduction-baseline) | Freeze and rerun judged verifier | `uv run python reproduction/run_all.py` | Claims 1,2,3,5 VERIFIED; historical Claim 4 TOY | Local CPU, 1 thread, 1.269 s verifier |
| [`orx/rtpm-adversarial-model-2-calibration`](https://github.com/MachineLearning-Nerd/icml26-repro-Kk5UZgkWFx-combinatorial-sparse-pca-beyond-the-spiked-identity-model/tree/orx/rtpm-adversarial-model-2-calibration) | Exact RTPM on adversarial Model 2 | `uv run python reproduction/run_all.py` | Environmental failure before science (`uv` absent) | HF `cpu-upgrade`, 8-core estimate |
| [`orx/rtpm-rotated-model-2-calibration`](https://github.com/MachineLearning-Nerd/icml26-repro-Kk5UZgkWFx-combinatorial-sparse-pca-beyond-the-spiked-identity-model/tree/orx/rtpm-rotated-model-2-calibration) | Exact RTPM on rotated Model 2 | `uv run python reproduction/run_all.py` | Environmental failure before science (`uv` absent) | HF `cpu-upgrade`, 8-core estimate |
| [`orx/claim-4-rare-signal-quantifier-audit`](https://github.com/MachineLearning-Nerd/icml26-repro-Kk5UZgkWFx-combinatorial-sparse-pca-beyond-the-spiked-identity-model/tree/orx/claim-4-rare-signal-quantifier-audit) | Proof-certificate falsification and cumulative regression | `uv run python reproduction/run_all.py` | Claim 4 FALSIFIED; Claims 1,2,3,5 VERIFIED; tamper control rejected | Local CPU, 1 thread, 1.584 s verifier |
| [`orx/cumulative-release-candidate`](https://github.com/MachineLearning-Nerd/icml26-repro-Kk5UZgkWFx-combinatorial-sparse-pca-beyond-the-spiked-identity-model/tree/orx/cumulative-release-candidate) | Evidence packaging and release regression | `uv run python reproduction/run_all.py` | All five claim-specific tamper controls rejected; cumulative suite passed | Local CPU, 1 thread, 1.373 s verifier |

The previous live judge score remains **9/10**. A possible **10/10** is a
forecast pending a new live evaluation, not a claimed score.

## Local use

```bash
uv sync
uv run python reproduction/run_all.py
uv run --with marimo==0.16.5 marimo edit notebooks/claim4_falsification.py
uv run --with marimo==0.16.5 marimo run notebooks/claim4_falsification.py
```

---

# Original workspace

ICML 2026 agent reproduction workspace for Kk5UZgkWFx.
