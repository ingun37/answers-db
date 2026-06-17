```matlab
syms V rho
T = 11.2;
W = -17.5;
g = -9.8;
eq0 = W == V*rho*g;


rho_h2o = 1e3;


B = -(V * rho_h2o * g);


eq1 = B + T + W == 0;


sol = solve([eq0 eq1]);
```

volume

```matlab
double(sol.V)
```

```matlabTextOutput
ans = 6.4286e-04
```

density

```matlab
double(sol.rho)
```

```matlabTextOutput
ans = 2.7778e+03
```