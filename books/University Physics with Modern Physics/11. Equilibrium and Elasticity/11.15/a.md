``` matlab
clear;
syms deg
theta = deg2rad(deg);
Lx = cos(theta);
Ly = sin(theta);
L = [Lx; Ly];
syms w Tx Ty Px Py;
T = [Tx; Ty];
P = [Px; Py];
W = [  0   ; -w   ];
net_force = P + T + W + W;
eq0 = net_force(1) == 0;
eq1 = net_force(2) == 0;

strut_torque = cross([L/2;0], [W;0]);
t1_torque = cross([L;0], [T;0]);
t2_torque = cross([L;0], [W;0]);
net_torque = strut_torque + t1_torque + t2_torque;
eq2 = net_torque(3) == 0;
```

(a)

``` matlab
solution = subs(solve([eq0, eq1, eq2], [Tx, Px, Py]), [deg Ty], [30 0]);
eval(subs(solution.Tx, w, 1))
```

``` matlabTextOutput
ans = -2.5981
```

``` matlab
eval(subs(norm([solution.Px, solution.Py]), w, 1))
```

``` matlabTextOutput
ans = 3.2787
```

``` matlab
rad2deg(eval(atan(solution.Py/solution.Px)))
```

``` matlabTextOutput
ans = 37.5891
```

(b)

``` matlab
eq3 = Ty == Tx * tan(deg2rad(30));
solution = subs(solve([eq0, eq1, eq2, eq3], [Tx, Ty, Px, Py]), [deg], [45]);
eval(subs(norm([solution.Tx, solution.Ty]), w, 1))
```

``` matlabTextOutput
ans = 4.0981
```

``` matlab
eval(subs(norm([solution.Px, solution.Py]), w, 1))
```

``` matlabTextOutput
ans = 5.3843
```

``` matlab
rad2deg(atan(eval(subs(solution.Py/solution.Px, w, 1))))
```

``` matlabTextOutput
ans = 48.7650
```
