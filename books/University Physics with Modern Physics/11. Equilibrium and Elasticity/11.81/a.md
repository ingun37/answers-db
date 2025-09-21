``` matlab
clear;
syms N1y N2y Fx h
c = 0.52;
Wy = -950;
F1x = N1y*c;
F2x = N2y*c;

a = [-2;0];
c = [-1;0];
p = [0.5;-h];
solution = solve([ ...
    F1x + F2x + Fx == 0, ...
    N1y + N2y + Wy == 0, ...
    torque(a, [0;N1y]) + torque(c, [0;Wy]) + torque(p, [Fx;0]) == 0 ...
    ], [N1y, N2y, Fx]);
```

(a)

``` matlab
eval(subs(solution.N1y, 1.6))
```

``` matlabTextOutput
ans = 79.8000
```

``` matlab
eval(subs(solution.N2y, 1.6))
```

``` matlabTextOutput
ans = 870.2000
```

(b)

``` matlab
x = 1.6:0.1:3;
plot(x, subs(solution.N1y, x), x, subs(solution.N2y, x))
eval(solve(solution.N1y == 0))
```

``` matlabTextOutput
ans = 1.9231
```
