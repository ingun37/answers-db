```matlab
clear;
syms D0 D1 positive
A0 = (D0/2)^2 * pi;
A1 = (D1/2)^2 * pi;
sol = solve(125/A0 == 1520*9.8 / A1, D0, Real=true);
sol = sol(1);
sol = simplify(D1 / sol);
double(sol)
```

```matlabTextOutput
ans = 10.9164
```