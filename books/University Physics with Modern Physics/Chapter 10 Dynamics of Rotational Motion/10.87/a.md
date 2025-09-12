```matlab
clear;
v=[2.8;0;0];
m=55;
It=80;
r=3;
wt=0.2;
xyz=cross([0;r;0], m*v);
Lr = xyz(3);
Lt = It * wt;
syms w
eval(solve((It + m * r ^ 2)*w == Lr + Lt, w))
```