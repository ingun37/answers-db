``` matlab
clear;
syms Ey Sy
E = [0;Ey;0];
a = [1;0;0];
S = [0;Sy;0];
B = [0;-280;0];
D = [0;-500;0];
L = [3;0;0];

NetF = (E + S + B + D);
eq0 = NetF(2) == 0;
torq0 = cross(a, S);
torq1 = cross(L/2, B);
torq2 = cross(L, D);

NetTorq = torq0 + torq1 + torq2;
eq1 = NetTorq(3) == 0;
solve([eq0 eq1], [Ey, Sy])
```

``` matlabTextOutput
ans = struct with fields:
    Ey: -1140
    Sy: 1920

```
