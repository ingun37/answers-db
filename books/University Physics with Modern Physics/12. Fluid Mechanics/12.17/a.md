```matlab
clear;
rho = 1.03e3;
h = 30;
g = 9.8;
atm = 1.013e5;
p = atm + rho * h * g;


A = 0.75;
W = 300;


syms F


eq = (F+W)/A + atm == p;
solve(eq)
```

ans = 226815