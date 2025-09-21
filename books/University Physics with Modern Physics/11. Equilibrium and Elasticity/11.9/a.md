``` matlab
clear;
syms lx Wy
F1y = 400;
F2y = 600;
Lx = 2;
F1 = [0; F1y; 0];
F2 = [0; F2y; 0];
L = [Lx; 0; 0];
W = [0; Wy; 0];
l = [lx; 0; 0];
```

(a)

``` matlab
LxF2 = cross(L, F2);
lxW = cross(l, W);
eq0 = LxF2(3) + lxW(3) == 0;
eq1 = Wy == -(F1y + F2y);
solve([eq0 eq1], [lx Wy])
```

``` matlabTextOutput
ans = struct with fields:
    lx: 6/5
    Wy: -1000

```

(b)

``` matlab
By = -200;
B = [0; By; 0];
torque2 = cross(L/2, B);
eq0 = LxF2(3) + lxW(3) + torque2(3) == 0;
eq1 = Wy + F1y + F2y + By == 0;
solve([eq0 eq1], [lx Wy])
```

``` matlabTextOutput
ans = struct with fields:
    lx: 5/4
    Wy: -800

```
