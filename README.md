# Combinatorial Sparse PCA Beyond the Spiked Identity Model — independent reproduction

[![Open in Molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-combinatorial-sparse-pca-beyond-spiked-identity-model/blob/main/notebooks/claim4_falsification.py)

Independent reproduction and claim audit for **Combinatorial Sparse PCA
Beyond the Spiked Identity Model** by Syamantak Kumar, Purnamrita Sarkar,
Kevin Tian, and Peiyuan Zhang.

- Paper: [arXiv:2603.02607](https://arxiv.org/abs/2603.02607)
- Exact scientific source audited here: [arXiv:2603.02607v1](https://arxiv.org/abs/2603.02607v1)
- Clean repository: [MachineLearning-Nerd/icml26-combinatorial-sparse-pca-beyond-spiked-identity-model](https://github.com/MachineLearning-Nerd/icml26-combinatorial-sparse-pca-beyond-spiked-identity-model)
- Hugging Face release: [DineshAI/Kk5UZgkWFx](https://huggingface.co/spaces/DineshAI/Kk5UZgkWFx)
- Reproduction command: `uv run python reproduction/run_all.py`

## What the paper does

The paper studies sparse PCA when the covariance is not restricted to the
spiked identity model. It gives explicit covariance counterexamples for
standard combinatorial methods, then proposes a truncated power method
(RTPM) with a global guarantee for general covariance. The paper also
extends the method to sparse leading eigenspaces and evaluates the methods
on synthetic and real sparse PCA data.

## Reproduction status

The current release contains five claim contracts. Four are verified and
the exact scale-free informal RTPM theorem wording is falsified. This is a
scoped scientific result: formal Theorem 2 is not contradicted because it
contains the signal-scale factor omitted by informal Theorem 1.

| Release result | Meaning |
| --- | --- |
| Claims 1, 2, 3, and 5: **VERIFIED** | The construction, model audit, required metric, and claim-specific control pass. |
| Claim 4: **FALSIFIED** | An assumption-satisfying rare-signal counterexample bounds success by `0.05` at `delta=0.1`, below the required `0.9`. |
| Formal Theorem 2: not contradicted | Its sample bound includes `(sigma^2/lambda1)^2`; that larger requirement is outside the falsification scope. |
| Historical live judge: `9/10` | This remains the last judged score. |
| Possible `10/10`: forecast only | No new live judge result is claimed until the published revision is evaluated. |

The local source audit pins the judged claim scope to v1 and records the
retrieved source hash `f329134d72e6d53c5f7867f73cd346a61c5bbb6b6100e5b19547bc2fa363f739`.
The current arXiv page is linked above for discovery; it is not silently
substituted for the hash-pinned evidence source.

## Claim-to-evidence map

The cumulative runner is [`reproduction/run_all.py`](reproduction/run_all.py).
It constructs the paper's covariance families, executes each check, audits
Model 2 assumptions, and sends the resulting payload through an independent
checker. The saved cumulative result is
[`raw_results.json`](.openresearch/artifacts/cumulative/raw_results.json).

| Claim | Paper statement | How the result is produced | Verdict |
| --- | --- | --- | --- |
| 1. Diagonal thresholding | Diagonal thresholding can miss every true support coordinate despite a constant eigengap. | `diagonal_counterexample` creates a sparse top vector plus a decoy diagonal block; Gaussian samples are converted to an empirical covariance, the largest empirical diagonal entries are selected, and support overlap is checked at `s=3,5,8`. All overlaps are `0`; `sin²=1`. | **VERIFIED** |
| 2. Covariance thresholding | Covariance thresholding can return an estimate orthogonal to the sparse top vector. | `covariance_threshold_counterexample` creates signal and decoy blocks; the empirical covariance is hard-thresholded, its top eigenvector is computed, and `sin²` is checked at `s=15,20` with `n=72,000` and `128,000`. Both scores are `1.0`; the audited gap ratio is `0.72`. | **VERIFIED** |
| 3. Greedy correlation | Greedy correlation can recover at most one support coordinate, even with a correct seed. | `greedy_counterexample` constructs the population covariance; the verifier ranks coordinates using the squared-covariance score and checks support overlap at `s=4,6,8`. The overlap is exactly `1` in every setting. | **VERIFIED** |
| 4. Informal Theorem 1 / imported RTPM claim | Under Model 2, scale-free `n=Omega(s² log(s) log(d/delta))`, `r=Omega(s²)`, and `T=Omega(log s)` should achieve squared correlation at least `0.9` with probability at least `1-delta`. | `falsify_claim4.py` fixes arbitrary finite hidden constants, chooses `s=2`, and builds a bounded signed-coordinate distribution with rare-event mass `delta/(4n)`. The all-zero event makes all hidden top coordinates indistinguishable; a rational checker proves success `<= delta/2`. At `delta=0.1`, the bound is `<=0.05`. | **FALSIFIED** |
| 5. Deflation barrier | Deflation can produce a fully dense next top eigenvector. | `deflation_counterexample` constructs an approximate first eigenvector, projects the covariance, eigendecomposes the deflated matrix, and checks the next eigenvector's nonzero count at `d=8,12,20`. Counts equal the full dimension in every setting. | **VERIFIED** |

### How verdicts are produced

1. `run_all.py` builds the five claim payloads and records the exact paper
   version, seed, environment, and runtime.
2. `model_audit` checks PSD covariance, the eigengap, top-eigenvector
   residual, and sparsity where applicable.
3. The independent checker recomputes decisive metrics and rejects any
   status or value that violates the contract.
4. Five negative controls mutate one decisive metric per claim. Every
   tampered payload is rejected; see
   [`independent_checker.json`](.openresearch/artifacts/claim_4/independent_checker.json).
5. Claim 4 additionally recomputes exact rational inequalities for multiple
   finite hidden-constant choices and explicitly checks that formal Theorem
   2 is not being claimed as falsified.

The historical RTPM run is retained as **TOY** evidence only: it used a
spiked-identity covariance, reused one sample covariance at every iteration,
ran one trial per setting, and omitted the theorem's `log(s)` and `delta`
calibration. It is not the current Claim 4 verdict.

## Branches

`main` is the publication surface. The complete historical-to-clean mapping
and branch purposes are in [branch-audit.md](branch-audit.md).

| Clean branch | Purpose |
| --- | --- |
| `audit/judged-baseline` | Preserve and rerun the historical judged baseline. |
| `experiment/rtpm-adversarial-model-2` | Attempt exact RTPM calibration on an adversarial non-spherical Model 2 family. |
| `experiment/rtpm-rotated-model-2` | Attempt exact RTPM calibration on a rotated non-spherical Model 2 family. |
| `audit/claim-4-rare-signal` | Produce and audit the parameterized rare-signal falsification certificate. |
| `release/cumulative-candidate` | Package the cumulative release evidence and tamper regressions. |
| `release/cumulative-publication` | Publication pointer for the released Hugging Face revision. |

The two calibration branches stopped before scientific execution because
their default Hugging Face image lacked `uv`. They remain useful provenance
for the environment failure, but they are not evidence for or against RTPM.
Historical `orx/` names are recorded only in the branch audit.

## Repository map

| Path | Role |
| --- | --- |
| `reproduction/core.py` | Shared covariance constructions, Gaussian sampling, support metrics, and deflation helpers. |
| `reproduction/run_all.py` | Cumulative claim runner, model audits, independent checker, and five tamper controls. |
| `reproduction/falsify_claim4.py` | Parameterized Claim 4 counterexample and exact probability certificate. |
| `reproduction/check_falsification.py` | Independent Claim 4 checker. |
| `.openresearch/audit` | Paper-source hash, claim scope, logbook, command, and release audits. |
| `.openresearch/artifacts` | Contracts, raw results, controls, runtime records, and evaluator guides. |
| `reports/claim-by-claim` | Illustrated technical report and post-publication verification. |
| `space_release` | Reader-facing release pages and the visibility matrix mirrored to the Hugging Face Space. |
| `notebooks/claim4_falsification.py` | Self-contained marimo tutorial for the main falsification result. |

## Reproduce locally

```bash
uv sync
uv run python reproduction/run_all.py
```

The accepted cumulative run used Python `3.12.11`, NumPy `2.3.2`, seed
`260302607`, a one-thread BLAS cap, and local CPU. It completed in
`1.372549875` seconds, used eight visible logical CPUs with one active
thread, and cost `$0`. The scientific revision was
`0b244ce29d127cec8dcacc481c19d61c7278e00a`.

For the tutorial surface:

```bash
uv run --with marimo==0.16.5 marimo edit notebooks/claim4_falsification.py
uv run --with marimo==0.16.5 marimo run notebooks/claim4_falsification.py
```

## Scope and limitations

- Claims 1, 2, 3, and 5 reproduce explicit counterexample constructions
  and their finite checks; the finite trials do not independently prove
  their universal probability quantifiers.
- Claim 4 targets only the scale-free informal Theorem 1 wording and the
  imported claim contract. It does not contradict formal Theorem 2 or assess
  RTPM after adding a lower signal-scale assumption.
- The Claim 4 counterexample is bounded, mean-zero, and 1-sub-Gaussian but
  non-Gaussian; that is allowed by Model 2.
- The literal RTPM update divides by zero on an all-zero block. The proof
  also covers any deterministic or randomized fallback based only on the
  observed data, so the verdict does not depend on that implementation edge
  case.
- The historical judged score and the possible `10/10` are kept separate
  from the current evidence; only a live evaluator can change the score.
- This repository is an independent reproduction and is not author-endorsed.

## Citation

```bibtex
@article{kumar2026combinatorial,
  title={Combinatorial Sparse PCA Beyond the Spiked Identity Model},
  author={Kumar, Syamantak and Sarkar, Purnamrita and Tian, Kevin and Zhang, Peiyuan},
  journal={arXiv preprint arXiv:2603.02607},
  year={2026},
  doi={10.48550/arXiv.2603.02607}
}
```

## Thank you

Thank you to Syamantak Kumar, Purnamrita Sarkar, Kevin Tian, and Peiyuan
Zhang for developing and sharing this work. The explicit constructions,
theorem statements, and public release artifacts made it possible to audit
the standard combinatorial counterexamples separately from the RTPM
quantifier issue, and to report the formal Theorem 2 boundary honestly.

Documentation, cleanup, and independent verification in this repository are
maintained by [MachineLearning-Nerd](https://github.com/MachineLearning-Nerd).
That attribution applies to this reproduction work and does not change the
provenance of the paper or the authors' artifacts.
