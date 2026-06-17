```matlab
clear;
function out = bernoulli(p, density, y, v)
g = 9.8;
out = p + density * g * y + 1/2 * density * v^2;
end
atm = 1.013e5;
Pg = [0.5 1   2   3   4] .* atm;
R =  [5.4 6.5 8.2 9.7 10.9];
```

(a) Why it's linear

```matlab
syms p r rho h v t positive
h_hole = 0.5;
g=9.8;
c0 = bernoulli(p, rho, h, 0); % surface
c1 = bernoulli(atm, rho, h_hole, v);
t = solve((1/2)*g*t^2 == h_hole);
eq = c0==c1;
eq = subs(eq, v, r/t);
eq = isolate(eq, r^2)
```

eq = 
 $\displaystyle r^2 =\frac{10\,p-49\,\rho +98\,h\,\rho -1013000}{49\,\rho }$
 

```matlab
coefficients = coeffs(subs(rhs(eq)), p)
```

coefficients = 

  $$ \displaystyle \left(\begin{array}{cc} -\frac{49\,\rho -98\,h\,\rho +1013000}{49\,\rho } & \frac{10}{49\,\rho } \end{array}\right) $$ 
 

(a) plotting

```matlab
R_squared = R .^ 2;
plot(Pg, R_squared)
```

![figure_0.png](./p87_media/figure_0.png)

```matlab
coef2 = polyfit(Pg, R_squared, 1);
slope = coef2(1)
```

```matlabTextOutput
slope = 2.5349e-04
```

```matlab
intercept = coef2(2)
```

```matlabTextOutput
intercept = 16.3848
```

(b)

```matlab
density = double(solve(coefficients(2)==slope))
```

```matlabTextOutput
density = 805.0837
```

```matlab
height = double(solve(subs(coefficients(1), rho, density)==intercept, h))
```

```matlabTextOutput
height = 21.5317
```