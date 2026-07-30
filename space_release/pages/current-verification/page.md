# Current verification

This page supersedes the verifier preserved as **Historical rejected
baseline**. The exact scientific revision is
`0b244ce29d127cec8dcacc481c19d61c7278e00a`.

## Fixed command and pinned environment

```bash
uv run python reproduction/run_all.py
```

- Python `3.12.11`; NumPy `2.3.2`
- `uv.lock` SHA-256:
  `59466dcd43c530701e0365e73af840d3c3a834a3edab86ecc1175ed02b5bfac6`
- `pyproject.toml` SHA-256:
  `b98f078394dbe4f2fc0ce2f8771ceff5a1a113a2e7e761b5bd7680d51812db96`
- Seed `260302607`
- OpenResearch run `20f41602-dfe5-459c-b839-db1dc3518dd2`
- Local CPU; estimated 1 core; BLAS cap 1 thread; 8 logical CPUs visible
- Verifier runtime `1.372549875` seconds; orchestration duration 5 seconds
- Cost `$0`

Executable sources are stored in this Space:
[run_all.py](https://huggingface.co/spaces/DineshAI/Kk5UZgkWFx/blob/main/reproduction/run_all.py),
[core.py](https://huggingface.co/spaces/DineshAI/Kk5UZgkWFx/blob/main/reproduction/core.py),
[Claim 4 construction](https://huggingface.co/spaces/DineshAI/Kk5UZgkWFx/blob/main/reproduction/falsify_claim4.py),
and [independent Claim 4 checker](https://huggingface.co/spaces/DineshAI/Kk5UZgkWFx/blob/main/reproduction/check_falsification.py).
The [locked environment](https://huggingface.co/spaces/DineshAI/Kk5UZgkWFx/blob/main/uv.lock)
and [configuration](https://huggingface.co/spaces/DineshAI/Kk5UZgkWFx/blob/main/reproduction/config.json)
are visible beside them.

## Claim-by-claim result

| Claim | Exact contract and assumptions | Raw result | Control | Verdict |
|---|---|---|---|---|
| 1 | Lemma 1: under Model 2, diagonal thresholding can detect no true support coordinate with probability at least 1/2 despite constant gap | `s=3,5,8`: overlap `0`, `sin²=1.0`; model gap ratio `0.9` | Cumulative checker requires all three overlaps to be zero | **VERIFIED** |
| 2 | Lemma 3: covariance thresholding can return an orthogonal estimate with probability at least 1/2 | `s=15,20`: `sin²=1.0`; gap ratio `0.72`; `n=72000,128000` | Thresholds lie between erased signal and surviving decoy entries | **VERIFIED** |
| 3 | Lemma 4: greedy correlation recovers at most one support coordinate even with a correct seed | `s=4,6,8`: overlap exactly `1` | Population squared-covariance ranks every selected decoy above remaining support | **VERIFIED** |
| 4 | Informal Theorem 1: for every `δ∈(0,1)`, Model 2 RTPM succeeds with correlation² `≥0.9` and probability `≥1-δ` at scale-free `n=Ω(s²log(s)log(d/δ))`, `r=Ω(s²)`, `T=Ω(log s)` | At `δ=0.1`, assumption-satisfying construction certifies success `≤0.05` for every finite hidden-constant choice | Rare-event mass changed to `1/2`; independent checker rejects | **FALSIFIED** |
| 5 | Lemma 11: deflation can produce a fully dense next top eigenvector | `d=8,12,20`: nonzero count `8,12,20` | Checker requires nonzero count to equal each full dimension | **VERIFIED** |

Download the exact
[cumulative raw JSON](https://huggingface.co/spaces/DineshAI/Kk5UZgkWFx/resolve/main/evidence_current/cumulative_raw_results.json),
[Claim 4 raw JSON](https://huggingface.co/spaces/DineshAI/Kk5UZgkWFx/resolve/main/evidence_current/claim4_raw_result.json),
[checker output](https://huggingface.co/spaces/DineshAI/Kk5UZgkWFx/resolve/main/evidence_current/claim4_independent_checker.json),
and [negative-control output](https://huggingface.co/spaces/DineshAI/Kk5UZgkWFx/resolve/main/evidence_current/claim4_negative_control.json).

## Independent checker output

```json
{
  "passed": true,
  "failures": [],
  "all_tampered_evidence_rejected": true,
  "negative_controls": {
    "claim_1": "overlap 0 -> 1: rejected",
    "claim_2": "sin2 1 -> 0: rejected",
    "claim_3": "overlap 1 -> 2: rejected",
    "claim_4": "rare mass delta/(4n) -> 1/2: rejected",
    "claim_5": "support 8 -> 7: rejected"
  }
}
```

The verifier exits nonzero unless Claims 1, 2, 3, and 5 retain their accepted
statuses, the Claim 4 certificate passes every recomputed inequality, and the
tampered certificate is rejected.

## Limitations and deviations

- Claim 4 is FALSIFIED, not experimentally “verified.”
- The result targets the scale-free informal theorem / imported claim wording.
- Formal Theorem 2 is not contradicted; it contains
  `(sigma^2/lambda1)^2`.
- The result does not assess RTPM after adding a signal-scale lower bound.
- Two exact-RTPM calibration jobs on non-spherical Model 2 stopped before
  scientific execution because the default HF image lacked `uv`; they are not
  counted as evidence.
