# Release report and forecast

- Previous live judged score: `9/10`
- Conservative projected score range after the proposed change: `9–10/10`
- Best-supported possible new score: `10/10` **forecast, not a judge result**

| Claim | Current points | Possible points | Confidence | Evidence status | Basis and remaining risk |
|---|---:|---:|---|---|---|
| 1 | 2 | 2 | HIGH | VERIFIED | Existing full-credit construction reran with zero support overlap; only evaluator regression risk remains |
| 2 | 2 | 2 | HIGH | VERIFIED | Existing full-credit orthogonal thresholded estimate reran at both settings |
| 3 | 2 | 2 | HIGH | VERIFIED | Existing full-credit greedy decoy construction reran with overlap exactly one |
| 4 | 1 | 2 | HIGH | FALSIFIED | Proof-level, assumption-satisfying counterexample covers arbitrary finite hidden constants; risk is evaluator interpretation of informal versus formal theorem scope |
| 5 | 2 | 2 | HIGH | VERIFIED | Existing full-credit deflation construction reran with full support at all dimensions |

Current live total: `9/10`.

Conservative projected total score range: `9–10/10`.

Best-supported possible total: `10/10`, pending live judge evaluation.

Claim-by-claim confidence: all five **HIGH**. Claim 4 changed from historical
TOY evidence to **FALSIFIED** evidence. No claims remain BLOCKED.

Exact publication action: upload the allowlisted text files to the existing
Space `DineshAI/Kk5UZgkWFx`, preserving every existing judged path; verify the
new revision and hashes; then mirror the reader-facing text paths to GitHub
`main`. No second Space will be created.

## Baseline and experiment tree

- Baseline score: `9/10`
- Protected HF Head:
  `73842f56f85f03a75322509f496600e5776d49ad`
- Protected Judge Head:
  `73842f56f85f03a75322509f496600e5776d49ad`
- Frozen baseline:
  `orx/judged-reproduction-baseline@c472cd87588f49223e66d5be71310a79db596253`
- Winning branch:
  `orx/cumulative-release-candidate@0b244ce29d127cec8dcacc481c19d61c7278e00a`
- Winning run:
  `20f41602-dfe5-459c-b839-db1dc3518dd2`

Tree: frozen baseline → adversarial and rotated positive-calibration siblings;
the adversarial implementation → rare-signal quantifier audit → cumulative
release regression. The two HF calibration runs stopped before science because
the default image lacked `uv`. They are not evidence for or against Claim 4.

## Runtime and cost

| Work | Selected compute | Estimated / actual CPU | Runtime | Cost |
|---|---|---|---:|---:|
| Baseline regression | local | 1 core / 1-thread cap, 8 logical visible | 1.269 s verifier | `$0` |
| Adversarial calibration | HF `cpu-upgrade` | 8-core estimate / probe never ran | 10 s wrapper failure | Not reported by provider |
| Rotated calibration | HF `cpu-upgrade` | 8-core estimate / probe never ran | 10 s wrapper failure | Not reported by provider |
| Claim 4 quantifier audit | local | 1 core / 1-thread cap, 8 logical visible | 1.584 s verifier | `$0` |
| Release regression | local | 1 core / 1-thread cap, 8 logical visible | 1.373 s verifier | `$0` |

## Evidence and safety

- Raw cumulative data:
  `evidence_current/cumulative_raw_results.json`
- Claim 4 contract, source audit, method, raw result, checker, control,
  environment, and evaluation: `evidence_current/claim4_*`
- Exact commands: `evidence_current/command_log.md`
- Blind review: `evidence_current/prepublication_red_team.md`
- Exact text allowlist hashes: `SHA256SUMS.txt`

The exact judged file path set is a subset of the candidate path set. All
historical pages and assets except the three navigation surfaces
(`README.md`, `logbook.json`, `pages/index.md`) retain their judged hashes.
The old verifier remains reachable as **Historical rejected baseline**.

The upload allowlist contains 35 text files: Markdown, JSON, Python, TOML,
lock text, SVG, and `SHA256SUMS.txt`. It contains no binary files and no
deletions. The allowlisted-file secret scan passed.

## Release gates

All twelve gates passed: honest terminal verdicts; cumulative regression;
judge criticism answered; fixed-command regeneration; five negative controls;
no toy/full-scale mislabeling; historical reachability; valid logbook;
allowlist and hashes; secret scan; complete canonical traversal; and repeated
evaluator-blind review after the checker fix.
