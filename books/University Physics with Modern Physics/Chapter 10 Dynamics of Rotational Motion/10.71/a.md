```matlab
clear;
syms m R b a T g
Idisk = 1/2 * m * R^2;
I = Idisk * 2;
e1 = I/b*a + b*T == 0
e2 = 2*m*a - T == -2 * m * g
sol = solve([e1, e2], [a, T]);
sol.T
sol.a
```