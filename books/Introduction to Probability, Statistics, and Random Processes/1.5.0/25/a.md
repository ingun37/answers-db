Let $`A`$ be the event that a student gets an $`A`$, and $`C`$ the event that lives on campus. This statement is:

```math
P(A|C) = P(A)
```

is equivalent to:

```math
P(A|C^c) = P(A)
```

Because of the lemma that when $`A`$ and $`B`$ are independent events then $`A`$ and $`B^c`$ are independent as well.


Lefthand is:

```math
\begin{aligned}
  &P(A|C^c) \\
  &= \dfrac{P(A,C^c)}{P(C^c)} \\
  &= \dfrac{\dfrac{80}{600}}{\dfrac{400}{600}} = \dfrac{1}{5}
\end{aligned}
```

Righthand is:

```math
P(A) = \dfrac{120}{600} = \dfrac{1}{5}
```

Therefore $`A`$ and $`C`$ are independent.