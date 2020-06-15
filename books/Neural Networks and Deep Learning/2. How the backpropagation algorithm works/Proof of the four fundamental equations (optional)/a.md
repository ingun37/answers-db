### BP3

BP3 is

```math
\frac{\partial C}{\partial b^l_j} = \delta^l_j
```

By chain rule

```math
\frac{\partial C}{\partial b^l_j} = \frac{\partial z_j}{\partial b^l_j} \frac{\partial C}{\partial z_j}
```

Definition of $`z_j`$ is

```math
z_j = b_j + w_j a
```

where $`w_j`$ is weight matix's jth row. We can easily see that

```math
\frac{\partial z_j}{\partial b^l_j} = 1 \\
\rightarrow \frac{\partial C}{\partial b^l_j} = \frac{\partial C}{\partial z_j} = \delta^l_j
```

### BP4

BP4 is

```math
\frac{\partial C}{\partial w^l_{jk}} = a^{l-1}_k \delta^l_j
```

By chain rule

```math
\frac{\partial C}{\partial ^l_j} = \frac{\partial z_j}{\partial w^jk} \frac{\partial C}{\partial z_j}
```

Definition of $`z_j'$ is

```math
\begin{aligned}
z_j &= b_j + w_j \cdot a \\
    &= b_j + \sum w_{jk} a_k
\end{aligned}
```

Derivative of $`z_j`$ in terms of $`w_{jk}`$ is easily

```math
\begin{aligned}
&\frac{\partial z_j}{\partial w^jk} = a_k \\
&\rightarrow \frac{\partial z_j}{\partial w^jk} \frac{\partial C}{\partial z_j} \\
&= a_k \delta^l_j
\end{aligned}
```