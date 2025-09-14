```matlab
clear;
D=0.52;
m=50;
w=850*2*pi/60;
F=160;
T=7.5;
I=1/2 * m * (D/2)^2;
k=2*I*w / (T * D * F)
```