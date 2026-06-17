```matlab
clear;
A1 = 20 * (1.0e-3)^2 * pi;
A0 = (0.8e-2)^2 * pi;
v0 = 3;
syms v1


double(solve(A0 * v0 == A1 * v1))
```

```matlabTextOutput
ans = 9.6000
```