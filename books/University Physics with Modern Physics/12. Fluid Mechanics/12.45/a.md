```matlab
clear;
function out = bernoulli(p, density, y, v)
g = 9.8;
out = p + density * g * y + 1/2 * density * v^2;
end
syms v2 positive
atm = 1.013e5;
rho = 1.03e3;
double(solve(bernoulli(atm*3, rho, 11, 0) == bernoulli(0, rho, 0, v2)))
```

```matlabTextOutput
ans = 28.3848
```