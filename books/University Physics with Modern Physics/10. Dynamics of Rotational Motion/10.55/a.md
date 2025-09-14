```matlab
clear;
m=2;
R=0.05/2;
w=19200 * 2 * pi / 60;
theta = deg2rad(1e-6);
t=5 * 60 * 60;
tau = m * R^2 * w * theta / t
```