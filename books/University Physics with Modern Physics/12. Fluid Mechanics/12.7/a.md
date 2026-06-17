```matlab
clear;
g_mars = 3.71; % m/s^2
h = 0.5e3; % m
density = 1e3; % kg/m^3
guage_pressure = density * g_mars * h
```

```matlabTextOutput
guage_pressure = 1855000
```

```matlab
syms h_e
g_earth = 9.8;
sol = solve(density*g_earth*h_e == guage_pressure);
double(sol)
```

```matlabTextOutput
ans = 189.2857
```