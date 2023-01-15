We can construct another series $`r_k`$ by dividing $`t_k - b_1`$ by 2. It will look like

```math
r_k = {t_k - b_1 \over 2} = b_2 + 2b_4 + 4b_8 + \cdots + 2^{k-1}b_{2^k}
```

If $`t_k`$ diverses then for every real number $`M`$ there exists $`k`$ such that $`2M + b_1 < t_k`$, which means $`M < (t_k - b_1)/2  = r_k`$ therefore $`r_k`$ diverges.


Define $`s_m`$

```math
s_m = b_1 + b_2 + b_3 + \cdots + b_m
```

Fix $`m`$ and let $`k`$ be small enough to ensure $`2^k - 1 \leq m`$. Then, $`s_{2^k - 1} \leq s_m`$ and

```math
\begin{aligned}
r_k &= b_2 + (b_4 + b_4) + (b_8 + b_8 + b_8 + b_8) + \cdots + (b_{2^k}  + \cdots + b_{2^k})
\\
&\leq b_1 + (b_2 + b_3) + (b_4 + b_5 + b_6 + b_7) + \cdots + (b_{2^{k-1}} + \cdots + b_{2^k - 1})
\\
&=s_{2^k-1}
\\
&\leq s_m
\end{aligned}
```

Therefore $`s_m`$ diverges.