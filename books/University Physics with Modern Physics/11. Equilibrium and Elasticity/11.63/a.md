``` matlab
clear;
W=[0;-75 * 9.8];
pos_ball = [12.5/100;0];
syms x
T=[0;x];
pos_heel = [-4.6/100;0];

tor_W = cross([pos_ball;0], [W;0]);
tor_T = cross([pos_heel;0], [T;0]);
```

(b)

``` matlab
F = eval(solve(tor_W(3) == tor_T(3)))
```

``` matlabTextOutput
F = 1.9973e+03
```

(c)

``` matlab
A = 78 / 10^2 / 100^2;
tensile_stress = F/A
```

``` matlabTextOutput
tensile_stress = 2.5606e+07
```

``` matlab
syms d
tensile_strain = d / 0.25;
Y = 1470e6;
eval(solve(Y==tensile_stress/tensile_strain)) * 100 * 10
```

``` matlabTextOutput
ans = 4.3548
```
