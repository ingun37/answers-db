It's given that $`(s_k)`$ is bounded. Let's say the bond of $`(s_k)`$ is $`S`$. Then
```math
|s_k (y_k - y_{k+1})| < S (y_k - y_{k+1})
```

Also

```math
\sum_{k=1}^\infin (y_k - y_{k+1}) \rightarrow y_1
```

The following *bigger* summation converges.

```math
\sum_{k=1}^\infin S(y_k - y_{k+1})
=
S \sum_{k=1}^\infin (y_k - y_{k+1})
\rightarrow
Sy_1
```

Therefore, by Comparison Test, $`\sum_{k=1}^\infin |s_k (y_k - y_{k+1})|`$ converges. Therefore, by Absolute Convergence Test, $`\sum_{k=1}^\infin s_k (y_k - y_{k+1})`$ converges.