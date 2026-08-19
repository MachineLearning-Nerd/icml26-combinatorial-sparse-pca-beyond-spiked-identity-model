# Audit report

This repository is an independent reproduction and claim audit for
**Combinatorial Sparse PCA Beyond the Spiked Identity Model**.

The explicit diagonal-thresholding, covariance-thresholding, greedy
correlation, and deflation counterexamples are supported under scoped
contracts. The exact scale-free informal Theorem 1 / imported RTPM claim is
falsified by a parameterized rare-signal certificate: for `delta=0.1`, the
success probability is at most `0.05` for every finite choice of hidden
constants. Formal Theorem 2 is not contradicted because its sample bound
includes a signal-scale factor omitted by the informal statement.

Read the detailed report at
[`reports/claim-by-claim/report.md`](reports/claim-by-claim/report.md), the
post-publication verification at
[`reports/claim-by-claim/post-publication.md`](reports/claim-by-claim/post-publication.md),
and the reader-facing release pages under [`space_release`](space_release).

The branch roles and historical `orx/` to clean-name mapping are documented
in [`branch-audit.md`](branch-audit.md). Branch names describe evidence role;
they are not separate paper versions or author statements.

