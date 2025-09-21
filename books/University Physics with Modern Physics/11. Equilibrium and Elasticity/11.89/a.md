(a)

``` matlab
clear;
W1 = 480;
W2 = 360;
syms r w
r = solve((4*r)^2 + (3*r)^2 == 2^2);
r = r(r>0);
w = solve((4*w)^2 + (3*w)^2 == 1.5^2);
w = w(w>0);
B = [-4*r;-3*r];
C = [3*w;-4*w];

syms N1 N2 T Fx Fy Wp
D = B * ((B(2)*2+0.9)/B(2));
E = C * ((C(2)*2+0.9)/C(2));

torque_left_A_eq=...
    torque(B, [0;-W1]) + torque(B*2, [0;N1]) + ...
    torque(D, [T;0]) == 0;

torque_right_A_eq=...
    torque(C, [0;-W2]) + torque(C*2, [0;N2]) + ...
    torque(E, [-T;0]) == 0;

solution = solve([ ...
    torque_left_A_eq,...
    torque_right_A_eq,...
    N2-W1-W2+N1 - Wp == 0
    ], [N1, N2, T]);
```

(a)

``` matlab
N1 = double(subs(solution.N1, Wp, 0))
```

``` matlabTextOutput
N1 = 391.2000
```

``` matlab
N2 = double(subs(solution.N2, Wp, 0))
```

``` matlabTextOutput
N2 = 448.8000
```

(b)

``` matlab
T = double(subs(solution.T, Wp, 0))
```

``` matlabTextOutput
T = 322.5600
```

(c)

``` matlab
solution_F = solve([Fx + -T == 0, -Fy + -W2 + N2 == 0])
```

``` matlabTextOutput
solution_F = struct with fields:
    Fx: 8064/25
    Fy: 444/5

```

``` matlab
Fx = double(solution_F.Fx);
Fy = double(solution_F.Fy);
F = [Fx;Fy];
norm(F)
```

``` matlabTextOutput
ans = 334.5600
```

(d)

``` matlab
double(subs(solution.T, Wp, 800))
```

``` matlabTextOutput
ans = 936.9600
```
