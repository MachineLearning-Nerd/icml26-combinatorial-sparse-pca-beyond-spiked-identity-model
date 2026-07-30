# Reproduction command log

No credentials, token values, environment values, or generated wrappers are
recorded here.

## Orientation and source audit

```bash
orx skill
orx skill orx-experiment-tree
orx skill orx-evidence
orx skill orx-git
orx skill orx-compute
orx skill orx-lit
orx skill orx-reports
orx projects --json
orx projects
orx runs 576b4c3c-7798-40ea-a79d-68ba70300207
orx project view 576b4c3c-7798-40ea-a79d-68ba70300207
git branch -a
git status --short
git rev-parse HEAD
git ls-remote origin refs/heads/main
df -h .
orx paper 2603.02607 --full
orx lit "restarted truncated power sparse PCA Yuan Zhang"
orx paper 1112.2679 --full
```

The paper HTML was retrieved with an explicit
`OpenResearch-Reproduction/1.0` User-Agent from
`https://ar5iv.labs.arxiv.org/html/2603.02607`. The verdict dataset and both
Space snapshots were downloaded with `hf download` at their exact revisions.
Environment inspection printed names only, never values.

## Project and experiment tree

```bash
orx project edit 576b4c3c-7798-40ea-a79d-68ba70300207 --run-command 'uv run python reproduction/run_all.py'
orx create-experiment 576b4c3c-7798-40ea-a79d-68ba70300207 --title "Judged reproduction baseline"
orx create-experiment 576b4c3c-7798-40ea-a79d-68ba70300207 --title "RTPM adversarial Model-2 calibration" --parent da26eabc-de51-44ef-b17e-15da05cb71e0
orx create-experiment 576b4c3c-7798-40ea-a79d-68ba70300207 --title "RTPM rotated Model-2 calibration" --parent da26eabc-de51-44ef-b17e-15da05cb71e0
orx create-experiment 576b4c3c-7798-40ea-a79d-68ba70300207 --title "Claim 4 rare-signal quantifier audit" --parent cff15323-5ba8-4024-b092-1c0c1c876227
orx create-experiment 576b4c3c-7798-40ea-a79d-68ba70300207 --title "Cumulative release candidate" --parent c120d80c-2153-4f0d-b8b6-501e440f67ad
```

Each node was checked out with `git fetch origin && git checkout <branch>`,
then committed and pushed before execution.

## Formal runs

Every node inherited the exact command
`uv run python reproduction/run_all.py`.

```bash
orx exp run da26eabc-de51-44ef-b17e-15da05cb71e0 --backend local
orx exp wait da26eabc-de51-44ef-b17e-15da05cb71e0 --timeout 480
orx logs 042f3ed5-e226-4f36-8356-2020e5fc8886

orx exp run cff15323-5ba8-4024-b092-1c0c1c876227 --flavor cpu-upgrade
orx logs 6b111f96-de41-4163-a03d-afc25dd312a3

orx exp run ef57090c-9f54-4d05-9c2a-fce14d52b589 --flavor cpu-upgrade
orx logs e92206cc-e608-4c80-a622-0a898084de38

orx exp run c120d80c-2153-4f0d-b8b6-501e440f67ad --backend local
orx exp wait c120d80c-2153-4f0d-b8b6-501e440f67ad --timeout 480
orx logs 167a3642-d164-40e6-827a-651f42cc2911 --bytes 50000

orx exp run 4714916e-f5df-4f1c-af06-1c97ea872026 --backend local
orx exp wait 4714916e-f5df-4f1c-af06-1c97ea872026 --timeout 480
orx logs 20f41602-dfe5-459c-b839-db1dc3518dd2 --bytes 50000
```

The two HF jobs failed before scientific execution because the default image
did not contain `uv`. Attempts to resubmit with
`ghcr.io/astral-sh/uv:python3.12-bookworm` did not create runs because of HF
quota/provider and transient GitHub connectivity errors.

## Lightweight validation and candidate audit

```bash
uv sync --frozen
uv run python -m py_compile reproduction/*.py
uv run --with marimo==0.16.5 marimo check notebooks/claim4_falsification.py
xmllint --noout reports/claim-by-claim/images/*.svg
rsvg-convert <figure.svg> -o <temporary-preview.png>
git diff --check
python -m json.tool <json-file>
shasum -a 256 <allowlisted-file>
hf download DineshAI/Kk5UZgkWFx --repo-type space --revision 73842f56f85f03a75322509f496600e5776d49ad --local-dir <fresh-directory>
shasum -a 256 -c SHA256SUMS.txt
```

The evaluator traversal script read only the candidate `README.md`,
`logbook.json`, `pages/index.md`, reachable pages, linked in-Space code/raw
data, and report images. The old/new subset comparison used sorted file lists
and SHA-256 comparisons for preserved historical files. Secret scans inspected
the allowlisted text files by filename-only match reporting.
