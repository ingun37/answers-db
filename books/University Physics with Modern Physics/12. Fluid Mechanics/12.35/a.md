```matlab
clear;
syms rho V rho_unknown
g = -9.8;
W = rho * V * g;
eq0 = W  + 39.2 == 0;
eq1 = W - V*1000*g + 28.4 == 0;
eq2 = W - V * rho_unknown * g  +21.5 == 0;
double(solve([eq0 eq1 eq2]).rho_unknown)
```

```matlabTextOutput
ans = 1.6389e+03
```