```matlab
clear;
syms V positive
M = 40;
rho = M/V;
g = 9.8;
W = M * g;
rho_h2o = 1e3;
```

(a)

```matlab
eq = -W + (V*0.8)*rho_h2o*g == 0;
V = double(solve(eq))
```

```matlabTextOutput
V = 0.0500
```

(b)

```matlab
syms W_brick positive


eq = -W - W_brick + V*rho_h2o*g == 0
```

eq = 
 $\displaystyle 98-W_{\textrm{brick}} =0$
 

```matlab
solve(eq)
```

ans = 
 $\displaystyle 98$