It goes like up-and-down, up-and-down, ... forever. I'll first proove that the Nth up-and-down is a superset of the next up-and-down.

```math
\begin{align}
\begin{split}
a_{2n+1} > a_{2n+2}
& \implies 0 > - a_{2n+1}  + a_{2n+2}  \\
& \implies S_{2n} > S_{2n} - a_{2n+1}  + a_{2n+2} \\
& \implies S_{2n} > S_{2n+2}
\end{split} \\ 
\begin{split}
a_{2n+2} > a_{2n+3}
& \implies a_{2n+2} - a_{2n+3} > 0  \\
& \implies  S_{2n+1} + a_{2n+2}  - a_{2n+3} > S_{2n+1} \\
& \implies S_{2n+3} > S_{2n+1}
\end{split} \\
\end{align}
```

Let $`I_n = [S_{2n}, S_{2n+1}]`$. Then

```math
\begin{align}
I_{n+1} = [S_{2n+2}, S_{2n+3}]
\end{align}
```

\(1), (2), (3), (4) $`\implies I_n \supset I_{n+1} \supset I_{n+2} \supset \cdots `$.

By NIP, there exists at least one $`x \in I_n \cap I_{n+1} \cap I_{n+2} \cap \cdots`$.

The length of $`I_n`$ is $`a_{n+1}`$ which converges to zero.\
Therefore for any $`\varepsilon > 0`$ there exists $`N`$ such that $`\forall n > N`$, length of $`I_n`$ is less than $`\varepsilon`$.\
Therefore for each $`I_n`$, $`|S_{2n+1} - x| < \varepsilon`$ and $`I_n`$, $`|S_{2n} - x| < \varepsilon`$.\
Therefore both subsequence $`(S_{2n+1})`$ and $`(S_{2_n})`$ converges to $`x`$.\
Those two subsequences composes the whole sequence therefore $`(S_n)`$ converges.