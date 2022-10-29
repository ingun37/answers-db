```math
\begin{aligned}
& \sum_{j=m}^nx_jy_j
\\
= & \sum_{j=m}^n(s_j - s_{j-1})y_j
\\
= & \sum_{j=m}^n (s_jy_j - s_{j-1}y_j)
\\
= & \sum_{j=m}^n( s_jy_j - s_j y_{j+1} + s_j y_{j+1} - s_{j-1}y_j)
\\
= &
\sum_{j=m}^n ( s_jy_j - s_j y_{j+1}) +
\sum_{j=m}^n (s_j y_{j+1} - s_{j-1}y_j)
\\
\end{aligned}
```

If you expand the second term in the last equation

```math
\sum_{j=m}^n (s_j y_{j+1} - s_{j-1}y_j) \\
=
s_my_{m+1} - s_{m-1}y_m 
+ s_{m+1}y_{m+2} - s_{m}y_{m+1}
+ s_{m+2}y_{m+3} - s_{m+1}y_{m+2}
+ \cdots + s_ny_{n+1} - s_{n-1}y_n
```

it turns out things cancel each out and only

```math
s_ny_{n+1} - s_{m-1}y_m
```

remanins. Therefore

```math
\sum_{j=m}^nx_jy_j = s_ny_{n+1} - s_{m-1}y_m + \sum_{j=m}^n s_j(y_j - y_{j+1})
```
