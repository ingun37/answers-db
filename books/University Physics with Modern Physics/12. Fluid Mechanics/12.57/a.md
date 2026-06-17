```matlab
clear;
function out = torque(y)
p = 1e3 * 9.8 * y;
syms F dy
w = 4; % width in m
A = dy * w; % area
sol = solve(p == F/A, F);
F = [sol 0 0];
X = [0 (y-1) 0];
T = cross(X,F);
out = subs(T(3), dy, 1);
end
syms y
double(int(torque(y), 0, 2))
```

```matlabTextOutput
ans = -2.6133e+04
```