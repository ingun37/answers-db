``` matlab
clear;
syms F;
A = 3e-4;
Y = 1.4e10;
strain = 0.01;
```

(a)

``` matlab
Fmax = solve(Y == F / A / strain)
```

Fmax =
$`\displaystyle 42000`$

(b)

``` matlab
syms h
v = sqrt(2*9.8*h);
m = 70/2;
eval(solve(m * v / 0.030 == Fmax))
```

``` matlabTextOutput
ans = 66.1224
```
