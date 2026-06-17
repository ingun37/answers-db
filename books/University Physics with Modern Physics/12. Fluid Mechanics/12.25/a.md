```matlab
clear;
syms V rho
rho_h2o = 1e3;
g = 9.8;
W = 900;
eq0 = W / g == V * rho;
eq1 = (W - 20) / g == V * rho_h2o;
sol = solve([eq0 eq1]);
volume = double(sol.V)
```

```matlabTextOutput
volume = 0.0898
```

```matlab
density = double(sol.rho)
```

```matlabTextOutput
density = 1.0227e+03
```