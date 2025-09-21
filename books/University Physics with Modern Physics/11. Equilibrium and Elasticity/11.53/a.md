(a)

``` matlab
clear;
wei_sign = 28 * 9.8;
ten_wire = wei_sign / 2;
wei_beam = 16 * 9.8;
syms Tx Ty Hy

eq_y = -wei_sign - wei_beam + Ty + Hy == 0;

tor_T1_hin = cross([1.5 - 0.9;0;0], [0;-ten_wire;0]);
tor_cm_hin = cross([1.5/2;0;0],[0;-wei_beam;0]);
tor_T2_hin = cross([1.5;0;0], [0;-ten_wire;0]);
tor_T0_hin = cross([1.5;0;0], [Tx;Ty;0]);

eq_torque = tor_T1_hin(3) + tor_cm_hin(3) + tor_T2_hin(3) + tor_T0_hin(3) == 0;

len_cable = 2;
len_beam = 1.5;
h = sqrt(len_cable^2 - len_beam^2);
eq_trig = Ty/Tx == h/(-len_beam);

sol = solve([eq_y, eq_torque, eq_trig]);

eval(norm([sol.Tx, sol.Ty]))
```

``` matlabTextOutput
ans = 408.9273
```

(b)

``` matlab
eval(sol.Hy)
```

``` matlabTextOutput
ans = 160.7200
```
