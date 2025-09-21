``` matlab
clear;
syms theta
syms Tx M
T = [Tx;0];
W = [0;-9.8*M];
syms Hx Hy
H = [Hx;Hy];

netF = T + W + H;

rod_end = [cos(theta);sin(theta)];
tqT = cross([rod_end;0],[T;0]);
tqW = cross([rod_end/2;0],[W;0]);

netT = tqT + tqW;

solution = solve([
    netF(1) == 0,
    netF(2) == 0,
    netT(3) == 0
    ],[Tx,Hx,Hy])
```

``` matlabTextOutput
solution = struct with fields:
    Tx: -(49*M*cos(theta))/(10*sin(theta))
    Hx: (49*M*cos(theta))/(10*sin(theta))
    Hy: (49*M)/5

```

``` matlab

tension_eq = solution.Tx;
syms x
eq2 = subs(tension_eq, cos(theta)/sin(theta), x);

slope = diff(eq2);

eval(solve(slope == 30,M))
```

``` matlabTextOutput
ans = -6.1224
```
