```matlab
clear;
function out = bernoulli(p, density, y, v)
g = 9.8;
out = p + density * g * y + 1/2 * density * v^2;
end
g=9.8;
h=8;
v3=sqrt(2*g*h);
A3=0.016;
```

(a)

```matlab
v3*A3
```

```matlabTextOutput
ans = 0.2004
```

(b)

```matlab
syms p v2
A2 = 0.048;
atm = 1.013e5;
eq0 = bernoulli(atm, 1e3, 8, 0) == bernoulli(p, 1e3, 0, v2);
eq1 = A3*v3 == A2*v2;
sol = solve([eq0 eq1]);
atm - double(sol.p)
```

```matlabTextOutput
ans = -6.9689e+04
```