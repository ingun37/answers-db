Set of continuous functions $`f : [a,b] \rightarrow [a,b]`$ is bijective to set of continuous functions $`g : [0,1] \rightarrow [0,1]`$ because there's some bijective function:

```math
m:[0,1] \rightarrow [a,b]
```

(One of which would be $`m(x) = x(b-a) + a`$)

therefore $`f`$ and $`g`$ can be defined by each other. That means for any $`f`$ there exists $`g`$ such that:

```math
f(x) = m \cdot g \cdot m^{-1} (x)
```

If $`m^{-1} (x)`$ is the fixed point of $`g`$, for there is always one, then it becomes:

```math
\begin{aligned}
    f(x) &= m \cdot m^{-1} (x) \\
         &= x
\end{aligned}
```

Therefore if there's a fixed point for $`g`$, there's one for $`f`$ too.