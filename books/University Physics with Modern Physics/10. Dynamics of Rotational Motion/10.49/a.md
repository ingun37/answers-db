```matlab
clear;
L=1;
m=0.05;
I=1/3 * m * L^2;
m=0.01;
v=0.2;
p=m*v;
w=p/I
K0=1/2 * I *w^2;
K1=1/2 * m * v^2;
K=K0 + K1
```