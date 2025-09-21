``` matlab
w=3400;
L=20;
theta = deg2rad(40);
C = [-8;   0];
W = [0;   -w];
cm= [-L/2; 0];
syms f
F = [-cos(theta); sin(theta)] * f;
syms A [2 1]

force_eq_x = F(1) + A1 + W(1) == 0;
force_eq_y = F(2) + A2 + W(2) == 0;
CxF = cross([C;0], [F;0]);
cmXw = cross([cm;0],[W;0]);
torque_eq = CxF(3) + cmXw(3) == 0;

solution = solve([force_eq_x, force_eq_y, torque_eq], [f, A1, A2]);
eval(solution.f)
```

``` matlabTextOutput
ans = 6.6118e+03
```
