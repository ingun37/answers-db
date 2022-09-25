## 1. $`(x_n)`$ is decreasing.

### Proof (by Induction)

The base case is that $`x_0 = 3 > x_1 = 1`$

The induction step is that

```math
\begin{aligned}
& x_n > x_{n+1} \\
& \rightarrow -x_n < -x_{n+1} \\
& \rightarrow 4-x_n < 4-x_{n+1} \\
& \rightarrow \frac 1 {4-x_n} > \frac 1 {4-x_{n+1}}
\end{aligned}
```

... hence decrease (monotonic).

## 2. $`(x_n)`$ is bounded.

Let's express $`x_n`$ in fraction

```math
x_n = \frac {a_n} {b_n}
```

then $`x_{n+1}`$ is

```math
\begin{aligned}
& x_{n+1} \\
& = \frac 1 {4-x_n} \\
& = \frac 1 {4 - \frac {a_n} {b_n}} \\
& = \frac 1 {\frac {4b_n - a_n} {b_n}} \\
& = \frac {b_n} {4b_n - a_n} \\
& = \frac {4b_n - a_n + a_n} {4(4b_n - a_n)} \\
& = \frac 1 4 + \frac {a_n} {4(4b_n - a_n)} \\
\end{aligned}
```

$`0 \leq a_n \leq 4b_n`$ therefore

```math
0 \leq \frac {a_n} {4(4b_n - a_n)}
```

It means 1/4 is a lower bound.

(1) and (2) satisfys the Monotone Convergence Theorem. Therefore $`(x_n)`$ converges.