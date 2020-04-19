Let's define some events.

```math
\begin{aligned}
  &W = B_1 \cap B_4 \cap B_3 \\
  &X = B_1 \cap B_5 \cap B_3 \\
  &Y = B_2 \cap B_4 \cap B_3 \\
  &Z = B_2 \cap B_5 \cap B_3 \\
\end{aligned}
```

Following is true

```math
B_3 \cap A = W \cup X \cup Y \cup Z
```

Therefore

```math
P(B_3 \cap A) = P(W \cup X \cup Y \cup Z)
```

Do the *inclusion-exclusion*

```math
\begin{aligned}
  P(W \cup X \cup Y \cup Z) = &P(W) + P(X) + P(Y) + P(Z) \\
  &-P(W \cap X)
  -P(W \cap Y)
  -P(W \cap Z)
  -P(X \cap Y)
  -P(X \cap Z)
  -P(Y \cap Z) \\
  &+P(X \cap Y \cap Z)
  +P(W \cap Y \cap Z)
  +P(W \cap X \cap Z)
  +P(W \cap X \cap Y) \\
  &-P(W \cap X \cap Y \cap Z) \\
\end{aligned}
```

Put it in terms of $`B`$

```math
\begin{aligned}
  &P(B_1 \cap B_4 \cap B_3)
  +P(B_1 \cap B_5 \cap B_3)
  +P(B_2 \cap B_4 \cap B_3)
  +P(B_2 \cap B_5 \cap B_3) \\
  &-P(B_1 \cap B_4 \cap B_3   \cap B_5  )
  -P(B_1 \cap B_4 \cap B_3 \cap B_2    )
  -P(B_1 \cap B_4 \cap B_3 \cap B_2 \cap B_5  )
  -P(B_1 \cap B_5 \cap B_3 \cap B_2 \cap B_4  )
  -P(B_1 \cap B_5 \cap B_3 \cap B_2    )
  -P(B_2 \cap B_4 \cap B_3 \cap   B_5  ) \\
  &+P(B_1 \cap B_5 \cap B_3 \cap B_2 \cap B_4 )
  +P(B_1 \cap B_4 \cap B_3 \cap B_2 \cap     B_2 \cap B_5 \cap )
  +P(B_1 \cap B_4 \cap B_3 \cap   B_5   \cap B_2    )
  +P(B_1 \cap B_4 \cap B_3 \cap   B_5   \cap B_2    ) \\
  &-P(B_1 \cap B_4 \cap B_3 \cap   B_5   \cap B_2  ) \\
\end{aligned}
```

Each $`B_i`$ are independent.

```math
\begin{aligned}
  &P_1  P_4  P_3
  +P_1  P_5  P_3
  +P_2  P_4  P_3
  +P_2  P_5  P_3 \\
  &-P_1  P_4  P_3    P_5  
  -P_1  P_4  P_3  P_2    
  -P_1  P_4  P_3  P_2  P_5  
  -P_1  P_5  P_3  P_2  P_4  
  -P_1  P_5  P_3  P_2    
  -P_2  P_4  P_3    P_5   \\
  &+P_1  P_5  P_3  P_2  P_4 
  +P_1  P_4  P_3       P_2  P_5  
  +P_1  P_4  P_3    P_5    P_2    
  +P_1  P_4  P_3    P_5    P_2     \\
  &-P_1  P_4  P_3    P_5    P_2   \\
\end{aligned}
```

Some cancels each other.

```math
\begin{aligned}
  &P_1  P_4  P_3
  +P_1  P_5  P_3
  +P_2  P_4  P_3
  +P_2  P_5  P_3 \\
  &-P_1  P_4  P_3    P_5  
  -P_1  P_4  P_3  P_2    
  -P_1  P_5  P_3  P_2    
  -P_2  P_4  P_3    P_5   \\
  &+P_1  P_5  P_3  P_2  P_4 
\end{aligned}
```

Devide it by $`P(A)`$, which is the result from (a).