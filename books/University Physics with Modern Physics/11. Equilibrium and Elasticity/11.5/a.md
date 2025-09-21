``` matlab
syms M L rL mL rR mR cm
mass_vec = [M mL mR];
pos_vec = [0 -L/2-rL L/2+rR];
eq = dot(mass_vec, pos_vec) == cm * (M+mL+mR);
eval(subs(solve(eq, cm), [M L rL mL rR mR], [0.3 0.4 0.08 0.9 0.06 0.38]))
```

``` matlabTextOutput
ans = -0.0970
```
