I'll first prove that every $`S_{2n+1}`$ is upper bound of every $`(S_{2n})`$ and vice versa.

Say there's some $`S_{2n}`$ and $`S_{2m+1}`$.

If $`m<n`$ then

```math
S_{2m+1} \ge S_{2n-1} > S_{2n}
```

Therefore $`S_{2m+1}`$ is an upper bound of $`S_{2n}`$.

If $`n<m`$ then

```math
S_{2n} < S_{2m} < S_{2m+1}
```

Therefore $`S_{2m+1}`$ is an upper bound of $`S_{2n}`$.

Every $`S_{2n}`$ is a lower bound of $`(S_{2n+1})`$ in the same way.

Say $`x`$ is the supermum(leat upper bound) of $`S_{2n}`$ and $`y`$ the infimum(greatest lower bound) of $`S_{2n+1}`$. For any $`\varepsilon > 0`$ there exists $`N`$ such that  $`\forall n > N`$ holds $`a_n < \varepsilon`$. It means

```math
|x < y| < |x - S_{2n+1}|  < |S_{2n} - S_{2n+1}| < \varepsilon
```

Therefore $`x=y`$ therefore the whole sequence $`S_n`$ converge.