```matlab
syms M h 
D = 0.9;
V = (D/2)^2 * pi * h;
rho = 1.03e3;
g = -9.8;
W = M * g;
buoy_force = rho * V * -g;
eq = buoy_force == W;
h0 = solve(subs(eq, M, 950));
h1 = solve(subs(eq, M, 950 + 80));


double(h0-h1)
```

```matlabTextOutput
ans = 0.1221
```