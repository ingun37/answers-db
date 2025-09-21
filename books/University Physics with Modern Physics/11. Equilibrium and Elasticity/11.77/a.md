``` matlab
clear;
syms N_A_x N_C_x
syms N_B_y
cross2 = @(a,b) cross([a;0],[b;0]);
W_1_y = 75e-3 * -9.8;
W_2_y = 75e-3 * -9.8;
center_1 = [-1/2; -sqrt(3)/2];
center_2 = [1/2; sqrt(3)/2];

tq_W_1 = cross2(center_1, [0;W_1_y]);
tq_W_2 = cross2(center_2, [0;W_2_y]);

A = center_1 + [-1;0];
B = center_1 + [0;-1];
C = center_2 + [1;0];

tq_A = cross2(A, [N_A_x;0]);
tq_B = cross2(B, [0;N_B_y]);
tq_C = cross2(C, [N_C_x;0]);

eq_x = N_A_x + N_C_x == 0;
eq_y = N_B_y + W_1_y + W_2_y == 0;
net_tq = tq_W_1 + tq_W_2 + tq_A + tq_B + tq_C;
eq_tq = net_tq(3) == 0;

solution = solve([eq_x, eq_y, eq_tq]);
```

(a)

``` matlab
eval(solution.N_A_x)
```

``` matlabTextOutput
ans = 0.4244
```

``` matlab
eval(solution.N_B_y)
```

``` matlabTextOutput
ans = 1.4700
```

``` matlab
eval(solution.N_C_x)
```

``` matlabTextOutput
ans = -0.4244
```

(b)

``` matlab
eval(norm([solution.N_C_x; W_2_y]))
```

``` matlabTextOutput
ans = 0.8487
```
