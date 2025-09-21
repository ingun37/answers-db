``` matlab
clear;
L = 1.2;
```

(a)

``` matlab
len_wire = L / sqrt(3) * 2
```

``` matlabTextOutput
len_wire = 1.3856
```

(b)

``` matlab
syms Hx Hy Tx
H =[Hx;Hy];
wei_rod = [0;-2*9.8];
Ty = tan(deg2rad(30)) * -Tx;
T = [Tx; Ty];
wei_obj = [0;-90*9.8];
tor_wei_rod = cross([L/2;0;0],[wei_rod;0]);
tor_T = cross([L;0;0],[T;0]);
tor_wei_obj = cross([L;0;0],[wei_obj;0]);

sol = solve([ ...
    Hx + Tx  == 0,
    Hy + Ty + wei_obj(2) + wei_rod(2) == 0,
    tor_wei_rod(3) + tor_T(3) + tor_wei_obj(3) == 0
    ]);

mag_T = norm(subs(T, Tx, sol.Tx));

syms d
strain = d / len_wire;
A = pi * (2.5 / 1000)^2;
stress = mag_T / A;
aluminium_Y = 7e10;
eval(solve(aluminium_Y == stress / strain))
```

``` matlabTextOutput
ans = 0.0018
```
