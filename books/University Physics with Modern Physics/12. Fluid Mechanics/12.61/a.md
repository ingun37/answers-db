```matlab
syms h positive


rho_ice = 0.92e3;
rho_h2o = 1e3;
rho_gly = 1.26e3;
r = 3.5e-2;
A = r^2*pi;
m_ice = 0.180;


w = -m_ice * g;
syms h
buoy =rho_gly * h * A * g;
h0 = solve(w + buoy == 0);
h1 = solve(A * h * rho_h2o == m_ice);
(h1-h0)
```

ans = 
 $\displaystyle \frac{52}{1715\,\pi }$