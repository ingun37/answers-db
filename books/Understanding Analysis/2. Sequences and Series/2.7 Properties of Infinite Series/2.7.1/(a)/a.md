By Monotone Convergence Theorem, $`(a_n)`$ converges to 0 therefore for any $`\varepsilon > 0`$, $`\exist n`$ such that $`|a_m| \le \varepsilon`$ for all $`m > n`$.

I'll proove by induction.

# Base case

$`|S_n - S_n| \le \varepsilon`$ and $`|S_{n+1} - S_n| \le \varepsilon`$

## Proof

$`|S_n - S_n| = 0 \le \varepsilon`$ 

and

$`|S_{n+1} - S_n| = |a_{n+1}| \le \varepsilon`$

# Induction step

If

```math
\begin{align}
& |S_m - S_n| \le \varepsilon \\
& |S_{m+1} - S_n| \le \varepsilon
\end{align}

```

then

```math
\begin{aligned}
&|S_{m+1} - S_n| \le \varepsilon \\
&|S_{m+2} - S_n| \le \varepsilon
\end{aligned}
```

## Proof

There are two cases: $`|S_{m+1} - S_n|`$ ends with either $`+ a_{m+1}`$ or $`- a_{m+1}`$.

### When $`|S_{m+1} - S_n| = \pm a_{n+1} \cdots + a_{m+1}`$

```math

\begin{equation}
\begin{split}
|S_{m+2} - S_n|
&= \pm a_{n+1} \cdots + a_{m+1} - a_{m+2} \\
&= |S_{m+1} - S_n| - a_{m+2}
\end{split}
\end{equation}

```

\(2) and (3) $`\implies |S_{m+2} - S_n| \le \varepsilon`$

### When $`|S_{m+1} - S_n| = \pm a_{n+1} \cdots - a_{m+1}`$

```math
\begin{equation}
\begin{split}
|S_{m+2} - S_n|
&= \pm a_{n+1} \cdots + a_m - a_{m+1} + a_{m+2} \\
&= |S_m - S_n| - a_{m+1} + a_{m+2} \\
\end{split}
\end{equation}
```

```math
\begin{align}
|a_{m}| < |a_{m+1}| \implies - a_{m+1} + a_{m+2} < 0
\end{align}
```

\(1) and (4) and (5) $`\implies |S_{m+2} - S_n| \le \varepsilon`$