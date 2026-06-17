```matlab
clear;
rho = 1e3;
g = 9.8;
h = 3;
A = 5 * 4;
p_bottom = rho * g * h;
```

(a)

```matlab
syms F_bottom
solve(p_bottom == F_bottom / A)
```

ans = 
 $\displaystyle 588000$
 

(b)

```matlab
syms y
p = rho * g * y;
w = 4;
int(p * w, 0, 3)
```

ans = 
 $\displaystyle 176400$