``` matlab
clear;
syms Tx Hx Hy
Ty =  Tx*-tan(deg2rad(10));
W = [0;-6490];
beam_dir_from_hinge = [cos(deg2rad(30));sin(deg2rad(30))];
tor_T = cross([beam_dir_from_hinge * 6;0],[Tx;Ty;0]);
tor_W = cross([beam_dir_from_hinge*7.5/2;0],[W;0]);
solution = solve([ ...
    Tx + W(1) + Hx == 0,
    Ty + W(2) + Hy == 0,
    tor_T(3) + tor_W(3) == 0
    ]);
Tx = solution.Tx
```

Tx =
$`\displaystyle -\frac{63281259101731520512}{1588212249228015\,\sqrt{3}+9007199254740992}`$

``` matlab
eval(eval(norm([Tx;Ty])))
```

``` matlabTextOutput
ans = 5.4650e+03
```
