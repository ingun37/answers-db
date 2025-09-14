```matlab
clear;
m=1/2;
v=2.25;
L=3/4;
angular_momentum_v3=cross([0;L*2/3;0],[v;0;0]*m);
ang_mom=angular_momentum_v3(3);
m=1.5;
I=1/3 * m * L^2;
```
(a)
```matlab
w0 = ang_mom/I
```
(b)
```matlab
syms w1
g=9.8;
e = 1/2 * I * w1^2 == 1/2 * I * w0 ^ 2 + L*m*g/2;
solution = solve(e, w1)
eval(solution(1))
```