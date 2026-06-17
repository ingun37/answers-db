```matlab
clear;
W0 = 45;
atm = 1.013e5;
D = 30e-2; % in m
A = (D/2)^2 * pi;
```

(a)

```matlab
W0/A
```

```matlabTextOutput
ans = 636.6198
```

(b)

```matlab
W1 = W0 + 83;
```

(i)

```matlab
h0 = 75e-2; % in m
g = 9.8;
rho = 0.850e-3; % in kg/cm^3
rho = rho / 1e6; % in kg/m^3
syms W h
eq = atm + (W/A) + h*g*rho;


dP = double(subs(eq, W, W1) - subs(eq, W, W0))
```

```matlabTextOutput
dP = 1.1742e+03
```

(ii)

dP doesnt' depend on h so the answer is the same as (i)