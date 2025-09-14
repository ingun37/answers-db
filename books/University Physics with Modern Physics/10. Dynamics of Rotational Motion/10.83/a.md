```matlab
clear;
syms Ia
Ib = Ia * 3;
syms w0 w1
eq0 = Ia * w0 == (Ia + Ib) * w1;
eq1 = 1/2*Ia*w0^2 - 1/2*(Ia+Ib)*w1^2 == 2400;
1/2 * Ia * solve([eq0, eq1], [w0, w1]).w0(2) ^ 2
```