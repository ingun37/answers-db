```math
|A_2| = 50 \\
|A_3| = 33 \\
|A_4| = 25 \\
|A_5| = 20
```

Following Inclusion-exclusion principle, i.e $`|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|`$

```math
\begin{aligned}
  &|A_2 \cup A_3 \cup A_5| \\
  &= |A_2| + |A_3| + |A_5| - |A_2 \cap A_3| - |A_2 \cap A_5| - |A_3 \cap A_5| + |A_2 \cap A_3 \cap A_5| \\
  &= |A_2| + |A_3| + |A_5| - |A_6| - |A_{10}| - |A_{15}| + |A_{30}| \\
  &= 50 + 33 + 20 - 16 - 10 - 6 + 3| \\
  &= 74
\end{aligned}
```