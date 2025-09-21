(a)

``` matlab
clear;
syms Hx Hy m g theta L alpha
Tx=-Hx;
Ty = -Tx*tan(theta);
W = [0;-m*g];
tor_W = cross([alpha * L;0;0],[W;0]);
tor_T = cross([L;0;0],[Tx;Ty;0]);
sol = solve([
    Hy + Ty + W(2) == 0,
    tor_W(3) + tor_T(3) == 0
    ], [Hx, Hy]);

simplify(atan(sol.Hy/sol.Hx))
```

ans =
$`\displaystyle -\textrm{atan}\left(\frac{\tan \left(\theta \right)\,{\left(\alpha -1\right)}}{\alpha }\right)`$

(b)

``` matlab
% by hand
% if beta equals theta then alpha is
1/2
```

``` matlabTextOutput
ans = 0.5000
```

(c)

``` matlab
% also by hand
0
```

``` matlabTextOutput
ans = 0
```
