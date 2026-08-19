# Environment and reproduction contract

## Fixed command

```bash
uv sync
uv run python reproduction/run_all.py
```

## Recorded accepted run

The accepted scientific revision was
`0b244ce29d127cec8dcacc481c19d61c7278e00a` with Python `3.12.11`, NumPy
`2.3.2`, seed `260302607`, one active BLAS thread, and eight visible logical
CPUs. The cumulative verifier runtime was `1.372549875` seconds and the
recorded cost was `$0`.

The locked environment hashes are recorded in
[`space_release/pages/current-verification/page.md`](space_release/pages/current-verification/page.md).
The raw cumulative result is
`.openresearch/artifacts/cumulative/raw_results.json`, and the source
command/environment record is under `.openresearch/artifacts/claim_4`.

The two exact-RTPM calibration branches stopped before science because the
default Hugging Face image lacked `uv`; their branches remain clearly labeled
as environment failures and are not counted as evidence.

This cleanup records and verifies the existing evidence bundle; it does not
silently replace it with an untracked rerun.

