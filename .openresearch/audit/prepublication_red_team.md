# Evaluator-blind pre-publication red team

## Review 1

Candidate base: exact judged revision
`73842f56f85f03a75322509f496600e5776d49ad` plus the draft text allowlist.

Files opened, in order:

1. `README.md`
2. `logbook.json`
3. `pages/index.md`
4. `pages/current-verification/page.md`
5. `pages/claim-4-falsification/page.md`
6. `pages/current-report/page.md`
7. the four linked report SVGs
8. `pages/visibility-matrix/page.md`
9. `pages/release-report/page.md`
10. linked `reproduction/*.py`, lock/config files, and raw/checker/control JSON
11. preserved historical pages

Finding: Claim 4 had a strong independent checker and negative control, but
Claims 1, 2, 3, and 5 only had status-string enforcement. Their results were
scientifically unchanged, but their visibility-matrix control cells were not
release-ready.

Fix: strengthen the cumulative checker to recompute the accepted metrics for
Claims 1, 2, 3, and 5. Add one claim-specific tamper per claim and require all
five tampered payloads to be rejected.

## Review 2

Candidate base: a new download of the exact judged revision plus the updated
allowlist generated from release run
`20f41602-dfe5-459c-b839-db1dc3518dd2`.

Files opened: the same ordered set as Review 1, without using the local
repository, OpenResearch logs, or unpublished branch knowledge.

Result:

- current verifier found first from the canonical entrypoint;
- all five exact claim contracts and verdicts found;
- fixed command, environment hashes, SHA, seed, CPU, runtime, and cost found;
- source code and downloadable raw JSON found inside the candidate;
- inline numbers matched raw JSON;
- independent checker output found;
- five claim-specific negative-control outputs found and all rejected;
- limitations distinguish informal Theorem 1 from formal Theorem 2;
- all four report images resolved and rendered;
- no conclusion required an inaccessible path;
- historical verifier appeared only as **Historical rejected baseline**.

Missing conclusions: none.
