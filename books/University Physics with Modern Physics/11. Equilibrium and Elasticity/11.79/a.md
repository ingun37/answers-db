``` matlab
clear;
W_y = 30 * -9.8;
W = [0;W_y];
W_mag = abs(norm(W));
syms beta c
N_norm = W_mag * cos(beta);
T_norm = W_mag * sin(beta);

F_max = N_norm * c;

x = 0:pi/64:pi/2;
% plot(x, subs(F_max, x), x, subs(T_norm, x))
slip_solution = solve(F_max == T_norm, beta, Real = true);
slip_point = rad2deg(slip_solution(1));

width = 0.25;
height = 0.5;
cg = rotate([width/2;height/2],beta);
% plot(x, subs(cg(1), x))
tipping_solution = solve(cg(1) == 0, beta, Real = true);
tipping_point = rad2deg(tipping_solution(1));
```

(a)

``` matlab
eval(subs(slip_point, 0.6))
```

``` matlabTextOutput
ans = 30.9638
```

``` matlab
eval(subs(tipping_point, 0.6))
```

``` matlabTextOutput
ans = 26.5651
```

(b)

``` matlab
eval(subs(slip_point, 0.4))
```

``` matlabTextOutput
ans = 21.8014
```

``` matlab
eval(subs(tipping_point, 0.4))
```

``` matlabTextOutput
ans = 26.5651
```
