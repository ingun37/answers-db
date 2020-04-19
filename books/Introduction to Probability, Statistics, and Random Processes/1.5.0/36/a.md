Let $`H`$ be the event that (n+1)th flip is head, $`H_n`$ the first $`n`$ flips are head, $`F`$ the picking the fake coin, $`R`$ the picking the real coin.

```math
\begin{aligned}
  &P(H|H_n) \\
  &= P((H \cap F) \cup (H \cap R) |H_n)
\end{aligned}
```

Since $`H \cap F`$ and $`H \cap R`$ are disjoint,

```math
\begin{aligned}
  &= P(H \cap F|H_n) + P(H \cap R|H_n) \\
  &= P(H |F,H_n)P(F|H_n) + P(H|R,H_n)P(R|H_n) &(1)
\end{aligned}
```

For the $`P(H |F,H_n)`$

```math
\begin{aligned}
  &P(H |F,H_n) \\
  &= \cfrac{P(H \cap F \cap H_n)}{P(F \cap H_n)} \\
  &= \cfrac{P((H \cap F) \cap (H_n \cap F))}{P(F \cap H_n)} \\
\end{aligned}
```

Since $`H \cap F`$, the fake coin landing *n+1*th flip head, and $`H_n \cap F`$, the fake coin landing first all *n* flips head, are independent

```math
\begin{aligned}
  &= \cfrac{P(H \cap F)P(H_n \cap F)}{P(F \cap H_n)} \\
  &= P(H \cap F) \\
  &= 1
\end{aligned}
```

For the same reason, $`P(H|R,H_n)`$ is 0.5. Now substitute them in *(1)*.

```math
\begin{aligned}
  &P(H|H_n) \\
  &= 1*P(F|H_n) + 0.5*P(R|H_n) &(2)
\end{aligned}
```

For the $`P(F|H_n)`$, use Bayes' rule.

```math
\begin{aligned}
  &P(F|H_n) \\
  &=\cfrac{P(H_n | F)P(F)}{P(H_n | F)P(F)+P(H_n|R)P(R)} \\
  &=\cfrac{1*0.5}{1*0.5+{0.5}^n*0.5} \\
  &=\cfrac{1}{1 + {0.5}^n} \\
\end{aligned}
```

For the same reason, $`P(R|H_n)`$ is $`\cfrac{{0.5}^n}{{0.5}^n+1}`$. Therefore the answer is

```math
\cfrac{1}{1 + {0.5}^n} + \cfrac{{0.5}^{n+1}}{{0.5}^n+1} = \cfrac{{0.5}^{n+1} + 1}{{0.5}^n+1}
```