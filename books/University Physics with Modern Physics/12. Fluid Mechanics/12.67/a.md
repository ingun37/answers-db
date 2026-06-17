```matlab
clear;
rho_h2o = 1e3;
g = 9.8;
Lx = 40;
Ly = 22;
Lz = 12 
```

```matlabTextOutput
Lz = 12
```

```matlab
V = Lx*Ly*Lz;
thickness = 4e-2;
rho_steel = 7.8e3;
V_wall_side = 2*(Lx+Ly)*Lz*thickness;
V_wall_bottom = Lx*Ly*thickness;
V_wall = V_wall_side + V_wall_bottom;


M_wall = V_wall * rho_steel;
W_wall = -M_wall * g;


syms M_coal positive
W_coal = -g * M_coal;
eq = W_wall + W_coal + (V*rho_h2o*g) == 0
```

eq = 
 $\displaystyle \frac{25836269253899063}{268435456}-\frac{49\,M_{\textrm{coal}} }{5}=0$
 

```matlab


M_coal = double(solve(eq))
```

```matlabTextOutput
M_coal = 9.8212e+06
```

```matlab


rho_coal = 1500e3;
V_coal = M_coal/rho_coal;


V > V_coal
```

```matlabTextOutput
ans = logical
   1


```