```matlab
clear;
syms m R F a
I0 = 1/2 * m * (2*R) ^ 2;
alpha0 = a / (2*R);
e0 = I0 * alpha0 == F * 2*R

syms T0
e1 = T0 - F == m * a

alpha1 = a / R;
I1 = 1/2 * m * R^2;
syms T1
e2 = I1 * alpha1 == T1*R - T0 * R

syms g
e3 = T1 - m*g == -m*a;

solution = solve([e0, e1, e2, e3], [a, F, T0, T1])
```