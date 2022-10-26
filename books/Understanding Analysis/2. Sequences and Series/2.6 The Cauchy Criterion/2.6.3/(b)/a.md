Given an $` \epsilon > 0`$, there exists an $` N `$ such that

```math
|x_n - x_m| < \epsilon \\
|y_n - y_m| < \epsilon
```
for all $`n > m \geq N`$.

Let $`\epsilon_x = x_n - x_m`$ and $`\epsilon_y = y_n - y_m`$.

Then

```math
\begin{aligned}
&
| x_ny_n - x_my_m |
\\
& = 
| (x_m + \epsilon_x)(y_m + \epsilon_y) - x_my_m | 
\\
& = 
| x_my_m + \epsilon_xy_m + x_m\epsilon_y + \epsilon_x\epsilon_y - x_my_m| 
\\
& = 
| \epsilon_xy_m + x_m\epsilon_y + \epsilon_x\epsilon_y | 
\\
& \leq
| \epsilon_xy_m | + | x_m\epsilon_y | + | \epsilon_x\epsilon_y | 
\\
\end{aligned}
```

Since $` |\epsilon_x| < |\epsilon| `$ and $` |\epsilon_y| < |\epsilon| `$

```math
\begin{aligned}
& \leq
| \epsilon y_m | + | x_m\epsilon | + \epsilon^2
\\
\end{aligned}
```

Cauchy sequence is bounded. Say bound of $`(y_n)`$ is $`Y`$ and $`(x_n)`$'s $`X`$.

```math
\cdots \\
\begin{aligned}
& \leq | \epsilon Y | + | X\epsilon | + |\epsilon^2 |
\end{aligned}
```

The last equation can be any real number. Therefore $`(x_ny_n)`$ is Cauchy sequence.