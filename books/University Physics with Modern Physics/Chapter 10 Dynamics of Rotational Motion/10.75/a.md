```matlab
clear;
h=50;
g=9.8
syms v0_pow2 v1_pow2
eq1 = g*h/2 == 1/5 * v0_pow2 + 1/2 * v0_pow2;
eq2 = g*h == 1/5 * v0_pow2 + 1/2 * v1_pow2;
result = solve([eq1, eq2], [v0_pow2, v1_pow2])
eval(sqrt(result.v1_pow2))
```