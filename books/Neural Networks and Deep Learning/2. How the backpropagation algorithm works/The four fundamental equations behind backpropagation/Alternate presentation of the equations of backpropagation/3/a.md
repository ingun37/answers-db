We've already proved that Hadamard productinng $`\sigma ' (z_l)`$ is equal to multiplying $`\Sigma ' (z_l)`$, and $`\Sigma ' (z_l)`$ can move it's multiplicative position. Rearranging the result of (2) we get

```math
\delta_l = W^\intercal \delta_{l+1} \odot \sigma ' (z_l) = W^\intercal \Sigma ' (z_l) \delta_{l+1}
```

which is recursive expression with the initial value of $`\delta^L = \Sigma'(z^L) \nabla_a C`$. We get the expression from the question when we serialize this recursive expression.