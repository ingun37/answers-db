```matlab
clear;
syms m L v w
Ib = m * (L/2)^2;
Ir = 1/3 * 4* m * L ^ 2;
I = Ib + Ir;
r = [0;L/2;0];
A=cross(r, m * [v;0;0])
eq = A(3) == -I * w
solve(eq, w)
cross([1;0;0],[0;1;0])
```