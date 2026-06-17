```matlab
clear;
syms h
rho = 1.03e3;
g = 9.8;
D = 8.2e-3; % m
A = (D/2)^2 * pi; % area of eardrum
double(solve(rho * h * g == 1.5 / A))
```

```matlabTextOutput
ans = 2.8139
```