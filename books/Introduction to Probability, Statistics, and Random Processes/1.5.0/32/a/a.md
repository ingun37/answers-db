Let's define each ways to get to $`B`$.

```math
\begin{aligned}
  &W = B_1 \cap B_4 \\
  &X = B_1 \cap B_3 \cap B_5 \\
  &Y = B_2 \cap B_3 \cap B_4 \\
  &Z = B_2 \cap B_5 \\
\end{aligned}
```

$`P(A)`$ can be defined in terms of them.

```math
P(A) = P(W \cup X \cup Y \cup Z)
```

Decompose using the *inclusion exclusion principle*.

```math
\begin{aligned}
  P(W \cup X \cup Y \cup Z) = &P(W) + P(X) + P(Y) + P(Z) \\
  &-P(W \cap X)-P(W \cap Y)-P(W \cap Z)-P(X \cap Y)-P(X \cap Z)-P(Y \cap Z) \\
  &+P(X \cap Y \cap Z)+P(W \cap Y \cap Z)+P(W \cap X \cap Z)+P(W \cap X \cap Y) \\
  &-P(W \cap X \cap Y \cap Z) \\
\end{aligned}
```

In terms of $`B_i`$

```math
\begin{aligned}
  &P(B_1 \cap B_4) + 
  P(B_1 \cap B_3 \cap B_5) + 
  P(B_2 \cap B_3 \cap B_4) + 
  P(B_2 \cap B_5) \\
  &-P(B_1 \cap B_4 \cap B_3 \cap B_5)
  -P(B_1 \cap B_4 \cap B_2 \cap B_3)
  -P(B_1 \cap B_4 \cap B_2 \cap B_5)
  -P(B_1 \cap B_3 \cap B_5 \cap B_2 \cap B_4)
  -P(B_1 \cap B_3 \cap B_5 \cap B_2)
  -P(B_2 \cap B_3 \cap B_4 \cap B_5) \\
  &+P(B_1 \cap B_3 \cap B_5 \cap B_2 \cap B_4)
  +P(B_1 \cap B_4 \cap B_2 \cap B_3 \cap B_5)
  +P(B_1 \cap B_4 \cap B_3 \cap B_5 \cap B_2)
  +P(B_1 \cap B_4 \cap B_3 \cap B_5 \cap B_2) \\
  &-P(B_1 \cap B_4 \cap B_3 \cap B_5 \cap B_2) \\
\end{aligned}
```

We can cancel out few things.

```math
\begin{aligned}
  &P(B_1 \cap B_4) + 
  P(B_1 \cap B_3 \cap B_5) + 
  P(B_2 \cap B_3 \cap B_4) + 
  P(B_2 \cap B_5) \\
  &-P(B_1 \cap B_4 \cap B_3 \cap B_5)
  -P(B_1 \cap B_4 \cap B_2 \cap B_3)
  -P(B_1 \cap B_4 \cap B_2 \cap B_5)
  -P(B_1 \cap B_3 \cap B_5 \cap B_2)
  -P(B_2 \cap B_3 \cap B_4 \cap B_5) \\
  &+P(B_1 \cap B_3 \cap B_5 \cap B_2 \cap B_4)
  +P(B_1 \cap B_4 \cap B_2 \cap B_3 \cap B_5)
\end{aligned}
```

Each $`B`$s are independent.

```math
\begin{aligned}
  &P_1  P_4 + 
  P_1  P_3  P_5 + 
  P_2  P_3  P_4 + 
  P_2  P_5 \\
  &-P_1  P_4  P_3  P_5
  -P_1  P_4  P_2  P_3
  -P_1  P_4  P_2  P_5
  -P_1  P_3  P_5  P_2
  -P_2  P_3  P_4  P_5 \\
  &+P_1  P_3  P_5  P_2  P_4
  +P_1  P_4  P_2  P_3 P_5
\end{aligned}
```