```matlab
clear;
syms rho_unknown
h_unknown = 35e-2;
h_gly = h_unknown - 12e-2;
rho_gly = 1.26e3;
double(solve(h_gly * rho_gly == h_unknown * rho_unknown))
```

```matlabTextOutput
ans = 828
```