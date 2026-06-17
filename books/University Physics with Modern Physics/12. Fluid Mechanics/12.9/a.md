```matlab
clear;
density = 1050; % kg/m^3
syms h
vein_pressure = 5980; % Pa = N/m^2
g = 9.8; % m/s^2
sol = solve(density * g * h == vein_pressure);
double(sol)
```

```matlabTextOutput
ans = 0.5811
```