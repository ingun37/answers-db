## Context

$`W`$ is a subspace of $`V`$

## $`\text{dim}W + \text{dim Ann}W = \text{dim}V`$

Let $`T : W \rightarrow V`$ be the projection linear transformation. (projection mapping maps $`x \in W`$ to $`x \in V`$ just like the identity mapping)  
There's a dual map $`T^* : V^*  \rightarrow W^*`$ defined as $`T^*(f) = f \circ T`$  
$`T^*`$ is linear because $`T`$ is linear therefore

```math
(f+g)\circ T = f\circ T + g\circ T \\
(cf)\circ T = c(f\circ T)
```

The definition of annihilator is exactly the same as the nullity of $`T^*`$, therefore $`\text{Ann}W`$ is a subspace of $`V`$.

Rank-nullity theorem says that $`\text{dim Nullity}T^* + \text{dim Rank}T^* = \text{dim}V `$.

1. Like I said before, Nullity of $`T^*`$ is $`\text{Ann}W`$ therefore $`\text{dim Nullity}T^* = \text{dim Ann}W`$.
2. $`T^*`$ is surjective therefore the rank is $`W^*`$. And $`W^*`$ is dual of $`W`$ therefore $`\text{dim Rank}T^* = \text{dim}W`$.

Therefore $`\text{dim Nullity}T^* + \text{dim Rank}T^* = \text{dim Ann}W + \text{dim}W = \text{dim}V `$.