# Claim 4 evaluation

Verdict: **FALSIFIED**

The scale-free informal Theorem 1 / imported Claim 4 requires success
probability at least `0.9` for `delta=0.1`. For every finite choice of the
hidden constants, the certificate constructs a bounded 1-sub-Gaussian
Model-2 instance on which success is at most
`delta/4 + 1/d <= 0.05`.

All Model-2 assumptions pass. The independent checker passes. A certificate
with its rare-event mass changed to `1/2` is rejected.

Formal Theorem 2 is not falsified because it includes the omitted
`(sigma^2/lambda1)^2` sample factor.
