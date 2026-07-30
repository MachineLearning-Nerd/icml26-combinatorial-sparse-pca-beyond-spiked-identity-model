# Claim 4 falsification method

Fix arbitrary finite hidden constants in the three asymptotic requirements,
then let those constants determine `n`, `r`, and `T`. Set `s=2` and choose
`d >= max(2r+1, 4/delta)`.

For a hidden top coordinate `j`, draw `X` from zero and the signed standard
basis vectors. Give coordinate `j` covariance eigenvalue `q`, every other
coordinate eigenvalue `0.9q`, and choose the total probability of any
nonzero observation to be `delta/(4n)`.

The distribution is mean-zero, norm-bounded by one, and therefore
1-sub-Gaussian by Hoeffding's lemma. It satisfies every Model-2 covariance,
gap, and sparsity assumption.

With probability at least `1-delta/4`, all `n` samples are zero. Conditional
on that event, the observations are identical for all `d` possible hidden
coordinates. Any unit output can correlate by at least `0.9` with at most one
standard basis vector, so at least one valid instance has conditional success
at most `1/d`. Its unconditional success is at most
`delta/4 + 1/d <= delta/2`, contradicting the required `1-delta`.

The executable checker recomputes every rational inequality. Its negative
control changes the rare-event mass to `1/2`; the checker must reject it.
