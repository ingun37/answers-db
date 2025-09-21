``` matlab
clear;
A_cm = 5e-3;
A_m = A_cm/10000; 
L = 1.5;
Y = 20e10;
M = 4.5;
syms dL F
strain = dL / L;
stress = F / A_m;
```

(a)

``` matlab
F0 = M*9.8;
dL0 = double(solve(subs(stress/strain, F, F0) == Y))
```

``` matlabTextOutput
dL0 = 6.6150e-04
```

(b)

``` matlab
dL1 = dL0+0.5/1000;
F1 = solve(subs(stress/strain, dL, dL1) == Y);
work_by_gravity = double(F0 * (dL1-dL0))
```

``` matlabTextOutput
work_by_gravity = 0.0221
```

(c)

``` matlab
work_by_varying_force = double((F1-F0) * (dL1-dL0)) / 2
```

``` matlabTextOutput
work_by_varying_force = 0.0083
```

(d)

``` matlab
-(work_by_varying_force + work_by_gravity)
```

``` matlabTextOutput
ans = -0.0304
```

(e)

``` matlab
F_by_x = solve(stress/strain == Y,F);
change = double(int(F_by_x, [dL0, dL1]))
```

``` matlabTextOutput
change = 0.0304
```
