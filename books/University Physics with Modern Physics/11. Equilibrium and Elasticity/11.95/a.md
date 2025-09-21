``` matlab
syms k T2x
W = 80 * 9.8;
T1x = 1160;
A = rotate([0;1.5], deg2rad(30));
B = rotate([0;1], deg2rad(30));
T2x0 = double(solve(torque(A, [T1x;0]) + torque(A, [T2x;0]) + torque(B, [0;-W])))
```

``` matlabTextOutput
T2x0 = -858.2383
```

``` matlab
f_max = k * W
```

f\_max =
$`\displaystyle 784\,k`$

``` matlab
k0 = 0.5
```

``` matlabTextOutput
k0 = 0.5000
```

``` matlab
k1 = 0.65
```

``` matlabTextOutput
k1 = 0.6500
```

``` matlab
k_x = [k0, k1];
T_diff = T1x + T2x0;
plot(k_x, subs(f_max, k_x), k_x, [T_diff, T_diff]);
```

\!\[figure\_2.png\](./chapter 11\_media/figure\_2.png)

``` matlab
disp('(d) feet will not slip')
```

``` matlabTextOutput
(d) feet will not slip
```
