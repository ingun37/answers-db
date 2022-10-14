Since $` (x_n) \rightarrow x `$, by definition of convergence, for all $` \epsilon`$ there exists $` N `$ such that $` N < n \Rightarrow |x_n - x | < \epsilon`$.

Let's say there's also $` m `$ that is bigger than $` N `$. That means

```math
\begin {aligned}
& |x_m - x| < \epsilon \\
& \Rightarrow |x - x_m| < \epsilon \\
& \Rightarrow |x - x_m| + |x_n - x| < 2\epsilon
\end {aligned}
```

And because of triangle equality

```math
\begin {aligned}
& \Rightarrow |x - x_m + x_n - x| = |x_n - x_m| < |x - x_m| + |x_n - x| < 2\epsilon
\end {aligned}
```
