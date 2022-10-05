Just zip the two geometrics series and geometric sequence.

```math
A_n = \frac 1 {2^n} = 
\left\{ \frac 1 2, \frac 1 4, \frac 1 8 \dots \right\}
```

```math
B_n = \sum \frac 1 {2^n} = 
\left\{ 
    \frac 1 2, \frac 3 4, \frac 7 8 \dots \right
    \}
```

Now the new sequence

```math
C_n = \begin{cases}
   A_n &\text{if } n \text{ is odd} \\
   B_n &\text{if } d \text{ is even}
\end{cases}
```

Now it's got two subsequences that converges to each 0 and 1.