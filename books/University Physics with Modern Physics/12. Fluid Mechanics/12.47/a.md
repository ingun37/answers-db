```matlab
clear;
function out = bernoulli(p, density, y, v)
g = 9.8;
out = p + density * g * y + 1/2 * density * v^2;
end
syms p
atm = 1.013e5;
rho = 1e3;
double(solve(bernoulli(p, rho, 0, 0) == bernoulli(atm, rho, 15, 0))) - atm
```

```matlabTextOutput
ans = 147000
```