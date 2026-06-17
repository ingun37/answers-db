```matlab
clear;
rho_hg = 13.6e3;
h_hg = 750e-3;
rho_wine = 990;
syms h_wine
double(solve(h_wine * rho_wine == h_hg * rho_hg))
```

```matlabTextOutput
ans = 10.3030
```