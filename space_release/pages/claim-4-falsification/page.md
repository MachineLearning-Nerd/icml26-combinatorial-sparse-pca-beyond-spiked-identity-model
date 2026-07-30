# Claim 4 falsification

## Exact statement under test

Informal Theorem 1
([paper anchor](https://ar5iv.labs.arxiv.org/html/2603.02607#Thmtheorem1))
states that, under Model 2, for `δ∈(0,1)`, RTPM with

- `n = Ω(s² log(s) log(d/δ))`,
- `r = Ω(s²)`, and
- `T = Ω(log s)`

returns `u` with `<v,u>² ≥ 0.9` with probability at least `1-δ`, in
`O(nd²)` time.

Model 2
([paper anchor](https://ar5iv.labs.arxiv.org/html/2603.02607#Thmmodel2))
requires i.i.d. 1-sub-Gaussian observations, PSD covariance, an at-most
`s`-sparse unit top eigenvector, and `λ₂≤0.9λ₁`. It states no positive lower
bound on `λ₁`.

Paper source retrieved 2026-07-30 from
`https://ar5iv.labs.arxiv.org/html/2603.02607`; SHA-256:
`f329134d72e6d53c5f7867f73cd346a61c5bbb6b6100e5b19547bc2fa363f739`.

## Counterexample for arbitrary hidden constants

Fix any finite positive constants hidden by the three `Ω` terms. They
determine finite `n`, `r`, and `T`. Set `s=2` and
`d≥max(2r+1,4/δ)`.

For each possible hidden top coordinate `j`, define a distribution on zero and
signed basis vectors:

- covariance eigenvalue `q` on coordinate `j`;
- covariance eigenvalue `0.9q` on every other coordinate;
- total probability of a nonzero observation `δ/(4n)`.

The distribution is symmetric and mean-zero. Every observation has norm at
most one. For every unit vector `u`, `<u,X>` lies in
`[-||u||∞,||u||∞]`; Hoeffding's lemma gives
`E exp(t<u,X>) ≤ exp(t²||u||∞²/2) ≤ exp(t²||u||₂²/2)`. Thus it is
1-sub-Gaussian. The covariance is PSD, `e_j` is a 1-sparse top eigenvector,
and `λ₂/λ₁=0.9`.

All `n` observations are zero with probability at least

`1 - n·δ/(4n) = 1-δ/4`.

On this event, the data are identical for all `d` hidden coordinates. A unit
output has squared correlation at least `0.9` with at most one basis vector.
By averaging over `j`, some valid instance has conditional success at most
`1/d`. Therefore

`P(success) ≤ δ/4 + 1/d ≤ δ/2`.

At `δ=0.1`, the certified upper bound is `0.05`, contradicting the required
`0.9`. This covers randomized defensive fallbacks as well as the literal
algorithm, which divides by zero when normalizing a zero truncated update.

## Machine-checked sanity instances

| Hidden constants `(sample,restarts,iterations)` | `(d,n,r,T)` | `P(all zero)` lower | `P(success)` upper | Required |
|---|---:|---:|---:|---:|
| `(1,1,1)` | `(40,17,4,1)` | `0.975` | `0.0500` | `0.9` |
| `(10,5,10)` | `(41,167,20,7)` | `0.975` | `0.04939` | `0.9` |
| `(100,25,50)` | `(201,2109,100,35)` | `0.975` | `0.02998` | `0.9` |

These finite rows are sanity checks. The proof is the parameterized
construction for arbitrary finite constants.

## Checker and negative control

The [independent checker](https://huggingface.co/spaces/DineshAI/Kk5UZgkWFx/blob/main/reproduction/check_falsification.py)
recomputes every rational probability bound and Model-2 condition. It passed
with no failures. Changing the first instance's nonzero mass from `δ/(4n)` to
`1/2` was rejected, so the checker does not accept every payload.

## Scope

Verdict: **FALSIFIED** for the scale-free informal Theorem 1 / imported
Claim 4.

Formal Theorem 2
([anchor](https://ar5iv.labs.arxiv.org/html/2603.02607#Thmtheorem2))
includes `(sigma²/lambda1)²` in the sample bound. The counterexample does not
satisfy that larger sample requirement, so formal Theorem 2 is not
contradicted.
