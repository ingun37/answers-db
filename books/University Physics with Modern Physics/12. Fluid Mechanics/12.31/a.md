```matlab
syms V
rho_rock = 1200;
W = -28;
g = -9.8;
V = solve(rho_rock * V *g == W);
syms T;


double(solve(T + W + -(V * 750 * g) == 0))
```

```matlabTextOutput
ans = 10.5000
```