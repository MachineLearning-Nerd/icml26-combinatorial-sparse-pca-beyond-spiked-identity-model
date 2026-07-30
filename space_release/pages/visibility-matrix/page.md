# Evidence visibility matrix

Audit starting only from `README.md`, `logbook.json`, and `pages/index.md`.

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | Current verification | Yes: `reproduction/core.py`, `run_all.py` | Yes | Cumulative raw JSON | Status and metric assertions | Required zero overlap across settings | Lemma 1 quantifiers and Model 2 gap | VERIFIED |
| 2 | Current verification | Yes: `reproduction/core.py`, `run_all.py` | Yes | Cumulative raw JSON | Status, angle, model audit | Threshold mechanism audit | Lemma 3 orthogonality claim | VERIFIED |
| 3 | Current verification | Yes: `reproduction/core.py`, `run_all.py` | Yes | Cumulative raw JSON | Status and overlap assertions | Decoy population ranking | Lemma 4 at-most-one claim | VERIFIED |
| 4 | Claim 4 falsification | Yes: construction and independent checker | Yes | Claim raw, checker, and control JSON | Recomputes rational inequalities | Tampered mass `1/2` rejected | Informal Theorem 1 assumptions and all finite hidden constants | FALSIFIED |
| 5 | Current verification | Yes: `reproduction/core.py`, `run_all.py` | Yes | Cumulative raw JSON | Status and full-support assertions | Requires support equal to each `d` | Lemma 11 dense-deflation claim | VERIFIED |

All rows also expose the fixed command, lockfile, scientific Git SHA, seed,
CPU/thread information, runtime, limitations, and deviations on
[Current verification](#/current-verification). No conclusion in this matrix
depends on an OpenResearch dashboard, an unpublished branch, or a hidden path.

Historical pages remain linked only under **Preserved history**. The obvious
current verifier is [Current verification](#/current-verification).
