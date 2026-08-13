# Branch audit

This repository began with OpenResearch-style `orx/` branch names. The
clean names below describe whether a branch is an audit, an experiment, or
a release surface. `main` remains the publication surface.

| Historical branch | Clean branch | Purpose and evidence scope |
| --- | --- | --- |
| `main` | `main` | Publication README, cumulative source tree, reports, and release pointers. |
| `orx/judged-reproduction-baseline` | `audit/judged-baseline` | Freezes and reruns the historical judged baseline; keeps its Claim 4 result labeled `TOY`. |
| `orx/rtpm-adversarial-model-2-calibration` | `experiment/rtpm-adversarial-model-2` | Attempts exact RTPM calibration on an adversarial non-spherical Model 2 family; stopped before science because `uv` was absent in the image. |
| `orx/rtpm-rotated-model-2-calibration` | `experiment/rtpm-rotated-model-2` | Attempts exact RTPM calibration on a rotated non-spherical Model 2 family; stopped before science because `uv` was absent in the image. |
| `orx/claim-4-rare-signal-quantifier-audit` | `audit/claim-4-rare-signal` | Audits arbitrary finite hidden constants and proves the rare-signal counterexample for the scale-free informal theorem. |
| `orx/cumulative-release-candidate` | `release/cumulative-candidate` | Packages the cumulative raw result, independent checker, five tamper controls, and evaluator-facing release evidence. |
| `release/cumulative-publication` | `release/cumulative-publication` | Publication pointer for the release that was mirrored to `DineshAI/Kk5UZgkWFx`. |

## Branch hygiene

- No historical `orx/` name remains in the cleaned public branch namespace.
- The historical names are retained in this file because they explain
  provenance and the old experiment tree.
- Branch names do not determine scientific verdicts; the contracts,
  verifiers, source audits, and controls do.
- The v1 paper scope and formal-Theorem-2 boundary are documented in
  [`.openresearch/audit/paper_source.md`](.openresearch/audit/paper_source.md)
  and the Claim 4 artifacts.
