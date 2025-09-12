```matlab
clear;
r=0.060;
I = 2.5;
syms t T;
F=5 * t;
tq = F * r;
angular_acc = tq / I
angular_vel = int(angular_acc,t)
angle = int(angular_vel, t)
t1=solve(8 * 2*pi==angle, t, Real=true)
eval(subs(F, t, t1))
```