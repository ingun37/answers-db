$`\delta_l`$ is gradient of $`C`$ in terms of $`z_l`$, namely

```math
\delta^l = \nabla_{z_l} C
```

Since $`a_l = \sigma(z_l)`$, we can apply chain rule with Jacobian matrix.

```math
\nabla_{z_l} C = {J_\sigma (z_l)}^\intercal \nabla_{a_l} C 
```

When the function is element-wise operation the Jacobian matrix becomes a diagonal matrix. $`\sigma`$ is elementwise function therefore the Jacobian matrix becomes exactly the matrix that was given in the problem.

```math
= {\Sigma' (z_l)}^\intercal \nabla_{a_l} C 
```

Transpose doesn't change diagonal matrices so

```math
= {\Sigma' (z_l)} \nabla_{a_l} C 
```