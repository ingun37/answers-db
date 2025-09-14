```matlab
clear;
m = 2.5;
m = 3.8;
g=9.8;
L = 0.8;
r = L/2;
h = L/2;
Istick = 1/12 * m * L^2;
Iball = m * r^2;
I = Istick + Iball;
tau = L / 2 * m * g;
```

(a)
```matlab
alpha = tau / I
```
(b)
```matlab
disp("no, decrease")
```
(c)
```matlab
wsquared = 2 * m * g * h / I;
w = sqrt(wsquared)
```