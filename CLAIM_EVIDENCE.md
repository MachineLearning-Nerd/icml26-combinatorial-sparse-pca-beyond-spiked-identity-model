# Claim-to-evidence ledger

Each verdict is produced by the cumulative runner, a claim-specific or
independent checker, saved raw evidence, and tamper controls. The exact
evaluator-facing tables are in
[`space_release/pages/current-verification/page.md`](space_release/pages/current-verification/page.md).

| Claim | Verdict | How the verdict is produced | Primary evidence |
| --- | --- | --- | --- |
| C1. Diagonal thresholding | `VERIFIED_SCOPED` | Construct a sparse top vector and decoy diagonal block, sample an empirical covariance, select the largest diagonals, and check zero support overlap at `s=3,5,8`. | [`reproduction/run_all.py`](reproduction/run_all.py) · [current verification](space_release/pages/current-verification/page.md) |
| C2. Covariance thresholding | `VERIFIED_SCOPED` | Construct signal and decoy blocks, hard-threshold the empirical covariance, compute its top eigenvector, and check `sin²=1` at `s=15,20`. | [`reproduction/run_all.py`](reproduction/run_all.py) · [current verification](space_release/pages/current-verification/page.md) |
| C3. Greedy correlation | `VERIFIED_SCOPED` | Build the population covariance, rank squared-covariance scores, and check support overlap exactly `1` at `s=4,6,8`. | [`reproduction/run_all.py`](reproduction/run_all.py) · [current verification](space_release/pages/current-verification/page.md) |
| C4. Informal Theorem 1 / imported RTPM claim | `FALSIFIED_SCOPED` | Fix arbitrary finite hidden constants, choose `s=2`, construct a rare-signal Model 2 distribution, and use an exact rational checker to certify success at most `delta/2`. | [`reproduction/falsify_claim4.py`](reproduction/falsify_claim4.py) · [`reproduction/check_falsification.py`](reproduction/check_falsification.py) · [Claim 4 page](space_release/pages/claim-4-falsification/page.md) |
| C5. Deflation barrier | `VERIFIED_SCOPED` | Construct an approximate first eigenvector, deflate the covariance, eigendecompose, and check a fully dense next top eigenvector at `d=8,12,20`. | [`reproduction/run_all.py`](reproduction/run_all.py) · [current verification](space_release/pages/current-verification/page.md) |

The five tamper controls mutate decisive values or statuses and are all
rejected by the independent checker. Claim 4's falsification is not an
experimental failure: it is a quantifier-level certificate for the exact
scale-free informal wording. The formal Theorem 2 boundary is checked and
explicitly left unclaimed.

