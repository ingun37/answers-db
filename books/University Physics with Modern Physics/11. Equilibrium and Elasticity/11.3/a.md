``` matlab
syms L M m l cm
mass_vec = [M; m];
pos_vec = [L/2; l];
eq = dot(mass_vec, pos_vec) == cm * (M + m);

eval(subs(solve(eq, l), [L M m cm], [2 1.8 2.4 1.2]))
```

``` matlabTextOutput
ans = 1.3500
```
