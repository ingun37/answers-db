```matlab
clear;
syms rho_B L rho_L
V = L^3;
m = V*rho_B;
g = 9.8;
w = m*g;
syms r_emerged
buoy = V*(1-r_emerged)*rho_L*g;
```

(a)

```matlab
solve(w == buoy, r_emerged)
```

ans = 
 $\displaystyle -\frac{\rho_B -\rho_L }{\rho_L }$
 

(b)

```matlab
rho_h2o = 1e3;
buoy_h2o = V*r_emerged*rho_h2o * g;
depth = L*solve(w == buoy + buoy_h2o, r_emerged)
```

depth = 
 $\displaystyle -\frac{L\,{\left(\rho_B -\rho_L \right)}}{\rho_L -1000}$
 

(c)

```matlab
double(subs(depth, [L rho_B rho_L], [0.1 7.8e3 13.6e3]))
```

```matlabTextOutput
ans = 0.0460
```