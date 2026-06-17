```matlab
rho_l = 11.3e3;
rho_a = 2.7e3;
syms M R_l R_a positive
V_l = R_l^3;
V_a = R_a^3;
eq = rho_l * V_l == rho_a * V_a;
sol = solve(eq, R_a, Real=true);
ratio = simplify( sol / R_l );
double(ratio)
```

```matlabTextOutput
Warning: The function sym/eval is deprecated and will be removed in a future release. Depending on the usage, use subs or double instead.
ans = 1.6115
```