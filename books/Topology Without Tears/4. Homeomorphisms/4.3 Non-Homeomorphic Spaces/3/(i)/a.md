Let's define a function.

```math
f : (0,1) \rightarrow X \backslash \{ \lang 1,0 \rang \} \\
f(x) = \lang \cos (2 \pi x), \sin (2 \pi x) \rang \\
```

1. $`f`$ is continuous because both $`\cos (2 \pi x)`$ and $`\sin (2 \pi x)`$ are continuous.  
2. $`f`$ is injective.

It's inverse can be defined using $`\text{atan2}`$.

```math
f^{-1} : X \backslash \{ \lang 1,0 \rang \} \rightarrow (0,1) \\
f^{-1}( \lang x,y \rang ) = \frac{\text{atan2}(y,x)}{2\pi}
```

3. $`f^{-1}`$ is continuous because $`\text{atan2}`$ is so.
4. $`f^{-1}`$ is injective.

By the statements 1,2,3, and 4 $`f`$ is homeomorphic.