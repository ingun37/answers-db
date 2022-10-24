Given $`\epsilon`$, there exits $`N`$ such that for all $`n`$ and $`m`$ that are bigger than $`N`$, e.i., $`N < m,n`$, following holds

```math
|x_n - x_m| = \epsilon_x < \epsilon \\
|y_n - y_m| = \epsilon_y < \epsilon
```

Then

```math
\begin{aligned}
& | x_ny_n - x_my_m | \\
& = | x_my_m - x_ny_n | \\
& = |(x_n+\epsilon_x)(y_n+\epsilon_y) - x_ny_n| \\
& = | \epsilon_xy_n + x_n\epsilon_y + \epsilon_x\epsilon_y | \\
& \leq | \epsilon_xy_n | + | x_n\epsilon_y | + |\epsilon_x\epsilon_y | \\
& \leq | \epsilon y_n | + | x_n\epsilon | + |\epsilon^2 |
\end{aligned}
```

Cauchy sequence is bounded. Say bound of $`(y_n)`$ is $`Y`$ and $`(x_n)`$'s $`X`$.

```math
\cdots \\
\begin{aligned}
& \leq | \epsilon Y | + | X\epsilon | + |\epsilon^2 |
\end{aligned}
```

The last equation can yield to any real number.