Just like the previous question, we can either prove it by using properties of diagonal matrices or applying one more chian rule to the answer of previous question. I'll go with latter one again.

Let $`T`$ be the function of multiplying and adding weights and biases.

```math
T(a) = Wa + B
```

Then we can define $`z_{l+1}`$ in terms of $`z_l`$.

```math
z_{l+1} = T \circ \sigma (z_l)
```

Jacobian of $`T \circ \sigma`$ is (chain rule)

```math
J_{T \sigma} = J_T (a_l) J_\sigma (z_l)
```

where $`J_\sigma (z_l)`$ is $`\Sigma ' (z_l)`$ (proven in the previous problem) and $`J_T (a_l) = W`$ (because of linearity). Therefore we can simplify like this

```math
= W \Sigma ' (z_l)
```

We are already given the gradient of $`C`$ in terms of $`z_{l+1}`$ which is $`\delta_{l+1}`$, therefore

```math
\begin{aligned}
    \delta_l &= \left( W \Sigma ' (z_l) \right)^\intercal \delta_{l+1} \\
             &= W^\intercal \Sigma ' (z_l)^\intercal \delta_{l+1} \\
\end{aligned}
```

Since $`\Sigma ' (z_l)`$ is diagonal we can remove the transpose and move it to the end and turn into Hadamard product.

```math
= W^\intercal \delta_{l+1} \odot \sigma ' (z_l)
```