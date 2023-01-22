Say a set of real numbers $`S`$ is upper-bounded. 

## When $`S`$ is finite

$`S`$ must have a maximum value. That's S's supermum.

## When $`S`$ is infinite

Choose one $`s \in S`$ and one upper bound $`B`$ of $`S`$. Define $`b = B - s`$. Define an interval $`I_n = [s, s+b]`$. Now recursively construct the next interval

```math
I_{n+1} = \begin{cases}
   [s', s' + b/2] &\text{if } \exist s' \in S\text{ such that } s+b/2 < s'\\
   [s, s+b/2] &\text{else}
\end{cases}

```

By *NIP*, there exists $`x`$ such that $`s < x < s + (1/2)^\infin`$ where $`s \in S`$ and $`s+(1/2)^\infin`$ is an upper bound. We already assumed that $`(1/2)^\infin \rightarrow 0`$, therefore for any upper-bound $`B = s+r`$, $`x < s+(1/2)^\infin < s+r = B`$, therefore $`x`$ is the supermum.

## Why precisely is this last assumption needed to avoid circularity?

AoC implies Archimedean Property. Archimediean Property implies Density of Q in R. Density of Q in R implies $`\exist n`$ such that $`0 < (1/2)^n < r`$ for any $`r \in \mathbb{R}`$.