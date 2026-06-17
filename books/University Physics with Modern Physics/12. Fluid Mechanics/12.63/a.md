```matlab
clear;
rho_h2o = 1e3;
h_h2o = 15e-2;
g=9.8;
```

(a)

```matlab
p = rho_h2o*g*h_h2o
```

```matlabTextOutput
p = 1470
```

(b)

```matlab
rho_Hg = 13.6e3;
syms h positive
eq = rho_Hg * g * (h_h2o - h) == p;
double(solve(eq))
```

```matlabTextOutput
ans = 0.1390
```