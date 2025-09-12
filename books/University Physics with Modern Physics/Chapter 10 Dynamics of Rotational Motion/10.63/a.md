```matlab
clear;
mA = 4;
mB = 2;
r = 0.12;
I = 0.22;
g = 9.8;
A = [1 0 mA; 0 1 -mB; r -r -I/r];
B = [mA*g;mB*g;0];
linsolve(A,B)
```