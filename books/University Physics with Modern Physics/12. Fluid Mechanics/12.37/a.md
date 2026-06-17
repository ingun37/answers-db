```matlab
clear;
M = 30;
rho = 370;
V = M / rho;
g = -9.8;
W = M * g;
B = V*0.7 * 1000 * g * -1; % buoy
syms T;
double(solve(T+B+W==0))
```

```matlabTextOutput
ans = -262.2162
```