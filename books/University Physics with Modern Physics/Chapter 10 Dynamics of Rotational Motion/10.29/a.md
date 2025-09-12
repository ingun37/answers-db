```matlab
clear()
v=6.66;
R1=20/100;
R2=35/100;
Rprime=R1^2+R2^2;
```
(a)
```matlab
g=9.8;
deno = 2*g;
numo = v^2 + 1/2*Rprime*v^2/R2^2;
h=numo/deno
```
(b)
```matlab
sqrt(2*g*h)
```