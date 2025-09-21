``` matlab
clear;
boom_weight = 2600;
BW = [0;-boom_weight];
crate_weight = 5000;
CW = [0;-crate_weight];
syms Tx
T = [Tx;0];
syms Px Py
P=[Px; Py];

net_force = BW + CW + T + P;

theta = deg2rad(60);
L = [cos(theta); sin(theta)];
T_t = cross([L;0],[T;0]);
BW_t = cross([L*0.35;0],[BW;0]);
CW_t = cross([L;0],[CW;0]);

net_torque = T_t + BW_t + CW_t;

eq0 = net_force(1) == 0;
eq1 = net_force(2) == 0;
eq2 = net_torque(3) == 0;

solution = solve([eq0, eq1, eq2]);
eval(solution.Tx)
```

``` matlabTextOutput
ans = -3.4121e+03
```

``` matlab
eval(solution.Px)
```

``` matlabTextOutput
ans = 3.4121e+03
```

``` matlab
eval(solution.Py)
```

``` matlabTextOutput
ans = 7600
```
