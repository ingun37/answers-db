``` matlab
clear;
syms Hx Hy
H=[Hx;Hy];
theta = asin(4/5);
T = 1000 * [-cos(theta);sin(theta)];
syms w
W = [0;-w];

net_force = H+T+W;

L=[9;0];
T_t = cross([L/3;0],[T;0]);
W_t = cross([L/2;0],[W;0]);
net_torque = T_t + W_t;

solution = solve([net_force(1)==0, net_force(2)==0, net_torque(3)==0]);
eval(solution.Hx)
```

``` matlabTextOutput
ans = 600
```

``` matlab
eval(solution.Hy)
```

``` matlabTextOutput
ans = -266.6667
```

``` matlab
eval(solution.w)
```

``` matlabTextOutput
ans = 533.3333
```
