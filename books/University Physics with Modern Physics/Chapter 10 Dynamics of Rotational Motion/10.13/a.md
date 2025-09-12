```matlab
m1=2;
m2=3;
s=1.2;
t=0.8;
g=9.8; 
a=2*s/t^2
T2=m2*g-m2*a
T1=m1*a
D=0.15;
R=D/2;
alpha = a/R
Ia = cro2([0;R],[-T1;0]) + cro2([R;0],[0;-T2])
Ia/alpha
```