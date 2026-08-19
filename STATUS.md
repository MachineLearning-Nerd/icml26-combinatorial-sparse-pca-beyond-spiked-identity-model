# Reproduction status

## Paper

**Combinatorial Sparse PCA Beyond the Spiked Identity Model** by Syamantak
Kumar, Purnamrita Sarkar, Kevin Tian, and Peiyuan Zhang. The canonical
scientific scope is arXiv `2603.02607v1`, pinned in the source audit.

## Overall verdict

`PARTIAL_CLAIMS_1_TO_3_AND_5_VERIFIED_CLAIM_4_SCALE_FREE_INFORMAL_RTPM_FALSIFIED`

Claims 1, 2, 3, and 5 pass their explicit construction and metric
contracts. Claim 4 is falsified only for the scale-free informal Theorem 1 /
imported RTPM wording: a bounded, mean-zero, 1-sub-Gaussian Model 2 family
certifies success at most `0.05` for `delta=0.1`, below the required `0.9`.
Formal Theorem 2 is not contradicted because its sample requirement contains
the signal-scale factor `(sigma^2/lambda1)^2`.

## Claim boundary

`C1_C2_C3_C5_SCOPED_VERIFIED_C4_SCALE_FREE_INFORMAL_THEOREM1_FALSIFIED_FORMAL_THEOREM2_NOT_CONTRADICTED`

| Item | Status |
| --- | --- |
| Current score claim | `false` |
| Publication gate | `false` |
| Official author endorsement | `false` |
| Last historical live judge | `9/10` |
| Possible next score | `10/10`, forecast only |

The historical score and forecast are context, never a current evaluator
result.

## Verification

The cumulative evidence was produced with:

```bash
uv sync
uv run python reproduction/run_all.py
```

The exact claim contracts, raw outputs, independent checker, tamper controls,
source audit, and limitations are linked from
[`CLAIM_EVIDENCE.md`](CLAIM_EVIDENCE.md).

