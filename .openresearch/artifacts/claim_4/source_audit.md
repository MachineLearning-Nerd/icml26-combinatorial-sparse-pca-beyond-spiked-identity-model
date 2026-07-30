# Claim 4 source audit

Retrieved 2026-07-30 from
`https://ar5iv.labs.arxiv.org/html/2603.02607` with SHA-256
`f329134d72e6d53c5f7867f73cd346a61c5bbb6b6100e5b19547bc2fa363f739`.

## Statement under test

Informal Theorem 1 (`#Thmtheorem1`) says that for every
`delta in (0,1)`, Algorithm 1 under Model 2 attains squared correlation at
least `9/10` with probability at least `1-delta` when
`n = Omega(s^2 log(s) log(d/delta))`, `r = Omega(s^2)`, and
`T = Omega(log(s))`.

Model 2 (`#Thmmodel2`) assumes i.i.d. 1-sub-Gaussian observations, PSD
covariance, an at-most-s-sparse unit top eigenvector, and
`lambda_2 <= 0.9 lambda_1`. It does not impose a positive lower bound on
`lambda_1`.

## Scale discrepancy

Formal Theorem 2 (`#Thmtheorem2`) includes the factor
`(sigma^2/lambda_k)^2` in its sample requirement. The informal theorem and
the imported Claim 4 contract omit it. The counterexample targets only that
scale-free informal statement.
