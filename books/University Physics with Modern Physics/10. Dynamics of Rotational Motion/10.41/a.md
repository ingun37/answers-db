```matlab
clear;
m=12;
r=48/2/100;
A=1.5;
B=1.1;
I=2/3*m*r^2;
```
(b)

(i)
```matlab
syms t
theta=A*t^2+B*t^4;
w=diff(theta, t);
L=I*w
eval(subs(L,[t],[3]))
```
(ii)
```matlab
torque=diff(L, t)
eval(subs(torque, t, 3))
```