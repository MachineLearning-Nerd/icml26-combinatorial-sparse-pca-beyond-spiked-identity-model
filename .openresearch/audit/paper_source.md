# Paper source audit

- Paper: *Combinatorial Sparse PCA Beyond the Spiked Identity Model*
- arXiv: `2603.02607v1`
- Retrieved: `2026-07-30` (Asia/Kolkata)
- URL: `https://ar5iv.labs.arxiv.org/html/2603.02607`
- Request User-Agent: `OpenResearch-Reproduction/1.0`
- Bytes: `933702`
- SHA-256: `f329134d72e6d53c5f7867f73cd346a61c5bbb6b6100e5b19547bc2fa363f739`
- Model 2 anchor: `#Thmmodel2`
- Informal Theorem 1 anchor: `#Thmtheorem1`
- Formal Theorem 2 anchor: `#Thmtheorem2`
- Lemma anchors: `#Thmlemma1`, `#Thmlemma3`, `#Thmlemma4`, `#Thmlemma11`

Model 2 fixes natural numbers `(s,d,n)` with `s <= d`; an unknown unit
`s`-sparse top eigenvector `v`; a positive-semidefinite covariance `Sigma`
with `lambda_2(Sigma) <= 0.9 lambda_1(Sigma)`; and i.i.d. samples from a
sub-Gaussian distribution with that covariance.

Theorem 1 quantifies over `delta in (0,1)`. For appropriate universal
constants, it assumes
`n = Omega(s^2 log(s) log(d/delta))`,
`r = Omega(s^2)`, and `T = Omega(log(s))`.
Algorithm 1 must use fresh sample blocks, all `d` standard-basis restarts,
top-`r` truncation at each step, and final empirical-Rayleigh selection.
It promises an `r`-sparse unit vector with squared correlation at least `9/10`
with probability at least `1-delta`, in `O(n d^2)` time.

The hidden constants make finite experiments corroborative rather than a
standalone proof. Current Claim 4 evidence therefore also requires a symbolic
audit of the Theorem 2 to Theorem 1 specialization.

