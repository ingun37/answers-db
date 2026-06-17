```matlab
clear;
rho_oil = 790;
g = -9.8;
```

(a)

```matlab
d = 1.5e-2;
p0 = d * g * rho_oil
```

```matlabTextOutput
p0 = -116.1300
```

(b)

```matlab
rho_h2o = 1000;
side = 10e-2;
p1 = side * g * rho_oil + d * g * rho_h2o
```

```matlabTextOutput
p1 = -921.2000
```

(c)

```matlab
syms rho
V = side ^ 3;
M = V * rho;
double(solve(M*g - g*side^2*(rho_h2o*d + rho_oil*(side-d))==0))
```

```matlabTextOutput
ans = 821.5000
```