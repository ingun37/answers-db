```matlab
clear;
function out = bernoulli(p, density, y, v)
g = 9.8;
out = p + density * g * y + 1/2 * density * v^2;
end
rho = 1e3;
syms v p
v0 = 2.5;
p0 = 1.8e4;
A0 = 1;
A1 = 2;
sol = solve([ ...
    v0*A0 == v*A1
    bernoulli(p0, rho, 1, v0) == bernoulli(p, rho, 1, v)
    ]);
double(sol.p)
```

```matlabTextOutput
ans = 2.0344e+04
```