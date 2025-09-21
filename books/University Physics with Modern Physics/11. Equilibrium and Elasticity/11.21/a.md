``` matlab
clear;
deg = 150;
syms T1mag
T1x = cosd(deg) * T1mag;
T1y = sind(deg) * T1mag;
T1 = [T1x; T1y];
syms T2x T2y
T2 = [T2x; T2y];
W = [0;-190];
M = [0;-90];
netF = T1 + T2 + W + M;
torqT1 = cross([-2.5;0;0],[T1;0]);
torqW = cross([-1;0;0],[W;0]);
torqT2 = cross([0.5;0;0],[T2;0]);
netT = torqT1 + torqT2 + torqW;

eqFx = netF(1) == 0;
eqFy = netF(2) == 0;
eqT = netT(3) == 0;

solution = solve([eqFx eqFy eqT], [T1mag T2x T2y]);
eval(solution.T1mag)
```

``` matlabTextOutput
ans = 220
```

``` matlab
eval(norm([solution.T2x, solution.T2y]))
```

``` matlabTextOutput
ans = 255.3429
```

``` matlab
rad2deg(eval(atan(solution.T2y/solution.T2x)))
```

``` matlabTextOutput
ans = 41.7415
```
