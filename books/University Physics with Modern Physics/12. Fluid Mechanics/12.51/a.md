```matlab
function out = bernoulli(p, density, y, v)
g = 9.8;
out = p + density * g * y + 1/2 * density * v^2;
end
clear;
dV_over_dt = 7200e-6;
rho = 1e3;
r0=4e-2;
p0=2.4e5;
r1=2e-2;
syms p1 v0 v1;
eq0 = dV_over_dt == r0^2*pi*v0;
eq1 = bernoulli(p0, rho, 1, v0) == bernoulli(p1, rho, 1, v1);
eq2 = dV_over_dt == r1^2*pi*v1;
sol = solve([eq0 eq1 eq2]);
double(sol.p1)
```

```matlabTextOutput
ans = 2.2461e+05
```