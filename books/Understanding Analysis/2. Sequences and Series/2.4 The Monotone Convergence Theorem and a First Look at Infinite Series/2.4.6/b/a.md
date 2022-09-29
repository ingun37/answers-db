$`(x)`$ is increasing and it can be prooven by induction.

The induction step is that if $`x_n < y_n`$ then $`x_{n+1} < x_{n+2}`$ because

```math
\begin {aligned}
& x_{n+2} \\
& = \sqrt{x_{n+1} y_{n+1}} \\
& = \sqrt{\sqrt{x_n y_n} \frac {x_n + y_n} 2}
\end {aligned}
```

Since it's prooven that arithmetic mean is bigger than geometric mean,

```math
\sqrt{x_n y_n} < \sqrt{\sqrt{x_n y_n} \frac {x_n + y_n} 2} \rightarrow x_{n+1} < x_{n+2}
```

$`(y)`$ is decreasing and it can be prooven in similar fashion.

$`x_n`$ and $`y_n`$ are each other's lower and higher bound therefore both sequence converges.

At the limit, $`\sqrt{\lim x_n \lim y_n} = \lim x_n`$ must be true therefore $`\lim x_n = \lim y_n`$.