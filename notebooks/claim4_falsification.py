import marimo

__generated_with = "0.16.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
        # A scale-sensitive counterexample for sparse PCA

        <svg xmlns="http://www.w3.org/2000/svg" width="760" height="250" viewBox="0 0 760 250">
          <rect width="760" height="250" rx="12" fill="#f8fafc"/>
          <text x="28" y="42" font-family="sans-serif" font-size="22" font-weight="700" fill="#172033">Claim 4 recovery probability</text>
          <rect x="90" y="82" width="250" height="92" rx="8" fill="#2563eb"/>
          <rect x="430" y="164" width="250" height="10" rx="5" fill="#dc2626"/>
          <text x="215" y="73" text-anchor="middle" font-family="sans-serif" font-size="22" font-weight="700" fill="#2563eb">≥ 90%</text>
          <text x="555" y="153" text-anchor="middle" font-family="sans-serif" font-size="22" font-weight="700" fill="#dc2626">≤ 5%</text>
          <text x="215" y="205" text-anchor="middle" font-family="sans-serif" font-size="16" fill="#172033">informal theorem requires</text>
          <text x="555" y="205" text-anchor="middle" font-family="sans-serif" font-size="16" fill="#172033">counterexample certifies</text>
          <text x="28" y="235" font-family="sans-serif" font-size="13" fill="#536174">δ = 0.1; proof-level bound, not a simulation estimate</text>
        </svg>

        The central question is whether the Restarted Truncated Power Method
        has a scale-free recovery guarantee over every distribution in Model 2.
        The answer for the informal statement as written is **no**.
        """
    )
    return


@app.cell
def _():
    from fractions import Fraction

    delta = Fraction(1, 10)
    instances = [
        {"C_n": 1, "d": 40, "n": 17},
        {"C_n": 10, "d": 41, "n": 167},
        {"C_n": 100, "d": 201, "n": 2109},
    ]
    return Fraction, delta, instances


@app.cell
def _(Fraction, delta, instances, mo):
    rows = []
    for instance in instances:
        d = instance["d"]
        n = instance["n"]
        total_nonzero = delta / (4 * n)
        all_zero_lower = 1 - n * total_nonzero
        success_upper = n * total_nonzero + Fraction(1, d)
        rows.append(
            {
                "sample constant": instance["C_n"],
                "d": d,
                "n": n,
                "all-zero probability ≥": f"{float(all_zero_lower):.3f}",
                "success probability ≤": f"{float(success_upper):.4f}",
                "required probability": f"{float(1-delta):.1f}",
            }
        )
    mo.vstack(
        [
            mo.md(
                r"""
                ## The construction

                After arbitrary finite hidden constants determine \(n,r,T\),
                choose \(s=2\) and \(d\geq\max(2r+1,4/\delta)\).
                For a hidden coordinate \(j\), sample zero most of the time and
                rare signed basis vectors otherwise. Set
                \(\lambda_j=q\), \(\lambda_k=0.9q\) for \(k\ne j\), and total
                nonzero mass to \(\delta/(4n)\).

                The distribution is mean-zero, norm-bounded by one, and thus
                1-sub-Gaussian. Its top eigenvector is the 1-sparse \(e_j\), and
                \(\lambda_2/\lambda_1=0.9\).
                """
            ),
            mo.ui.table(rows),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## The proof

        A union bound gives

        \[
        P(\text{all }n\text{ observations are zero})
        \geq 1-n\frac{\delta}{4n}=1-\frac{\delta}{4}.
        \]

        On this event, every hidden direction \(e_j\) produces identical data.
        Any unit output can have squared correlation at least \(0.9\) with at
        most one basis vector. Averaging over \(j\) therefore gives a valid
        instance with conditional success at most \(1/d\). Hence

        \[
        P(\text{success})\leq \frac{\delta}{4}+\frac1d
        \leq\frac{\delta}{2}=0.05,
        \]

        contradicting the required \(1-\delta=0.9\).

        This **FALSIFIES only the scale-free informal theorem / imported Claim
        4 wording**. Formal Theorem 2 includes
        \((\sigma^2/\lambda_1)^2\), so it is not contradicted.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        """
        ## Reproducibility

        The formal evidence command was:

        ```bash
        uv run python reproduction/run_all.py
        ```

        Scientific revision:
        `0b244ce29d127cec8dcacc481c19d61c7278e00a`.
        The cumulative verifier reran Claims 1, 2, 3, and 5, checked this
        certificate independently, and rejected a deliberately corrupted
        rare-event mass. Runtime was 1.373 seconds on local CPU with one BLAS
        thread. Seed `260302607` is recorded; this proof itself is deterministic.
        """
    )
    return


if __name__ == "__main__":
    app.run()
