``` matlab
clear;
syms Tx Ay Bx By
Ty = tan(deg2rad(180 - 30)) * Tx;
A = [0;Ay];
T = [Tx;Ty];
Wy = -700;
W = [0;Wy];
C = [4;2];
cross2 = @(a,b) cross([a;0],[b;0]);
tq_T = cross2(C,T);
center = C/2;
tq_W = cross2(center, W);
Tx = solve(tq_T(3) + tq_W(3) == 0);
Ty = subs(Ty, Tx);
```

(a)

``` matlab
eval(norm([Tx;Ty]))
```

``` matlabTextOutput
ans = 375.1289
```

(b)

``` matlab
Bx = solve(Bx + Tx == 0);
eval(abs(Bx))
```

``` matlabTextOutput
ans = 324.8711
```

(c)

``` matlab
By = solve(Ay + By + Wy + Ty == 0);
eval(By + Ay)
```

``` matlabTextOutput
ans = 512.4356
```
