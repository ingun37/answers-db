```matlab
clear;
function out = bernoulli(p, density, y, v)
g = 9.8;
out = p + density * g * y + 1/2 * density * v^2;
end
syms Ad h1 g atm pc rho h2
Ac = Ad/2;
vd = sqrt(2*g*h1)
```

vd = 
 $\displaystyle \sqrt{2}\,\sqrt{g\,h_1 }$
 

```matlab
vc = Ad * vd / Ac;
eq0 = bernoulli(atm, 1e3, h1, 0) == bernoulli(pc, 1e3, 0, vc);
eq1 = pc + rho*g*h2 == atm
```

eq1 = 
 $\displaystyle \textrm{pc}+g\,h_2 \,\rho =\textrm{atm}$
 

```matlab
sol = solve([eq0 eq1], [h2 pc])
```

```matlabTextOutput
sol = struct with fields:
    h2: -(200*(49*h1 - 20*g*h1))/(g*rho)
    pc: atm + 9800*h1 - 4000*g*h1


```

```matlab
eval(subs(sol.h2, [g rho],[9.8 1e3]))
```

```matlabTextOutput
Warning: The function sym/eval is deprecated and will be removed in a future release. Depending on the usage, use subs or double instead.
```

ans = 
 $\displaystyle 3\,h_1 $