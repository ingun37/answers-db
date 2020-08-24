Let $`W`$ be a subspace of $`V`$. The annihilator of $`W`$, denoted $`\text{Ann}W`$, is the set of all linear functionals that map every element of $`W`$ to zero:

```math
\text{Ann} W := \{\theta \in V^* : \theta(w) = 0, \text{for all } w \in W\}
```

$`\text{Ann}W`$ is a subspace of $`V^*`$ and that every subspace of $`V^*`$ is $`\text{Ann}W`$ for
some $`W`$. In the process verify that $`\text{dim } V = \text{dim }W + \text{dim Ann }W`$. Hint: For the
second part, let $`U^*`$ be a subspace of $`V^*`$ and define

```math
W := \{v \in V : f(v) = 0, \text{for all } f \in U^*\}
```

Use this to show that $`U^* \subseteq \text{Ann }W`$. Equality then follows by a dimension argument.