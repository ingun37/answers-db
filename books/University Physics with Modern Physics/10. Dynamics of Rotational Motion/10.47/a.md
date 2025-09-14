(a)
```matlab
clear;
r=2;
m0=120;
w=3;
m1=70;
I0=1/2*m0*r^2;
I1=m1 * r^2;
w1 = w*I0/(I0+I1)
```
(b)
```matlab
before = 1/2 * I0 * w^2
after = 1/2 * (I1 + I0) * w1^2
```