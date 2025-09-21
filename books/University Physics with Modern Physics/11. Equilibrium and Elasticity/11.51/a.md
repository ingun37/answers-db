(a)

``` matlab
clear;
syms pos_W_left_x pos_ful_left_x
pos_W_left = [pos_W_left_x;0];
pos_ful_left = [pos_ful_left_x;0];
pos_W_ful = pos_W_left - pos_ful_left;
syms wei_W
tor_W_ful = cross([pos_W_ful;0], [0;-wei_W;0]);
pos_V_left = [2;0];
pos_V_ful = pos_V_left - pos_ful_left;
wei_V = 225;
tor_V_ful = cross([pos_V_ful;0], [0;-wei_V;0]);
wei_R = 255;
pos_ful_right = [-0.75;0];
pos_R_ful = [-1;0] - pos_ful_right;
tor_R_ful = cross([pos_R_ful;0], [0;-wei_R;0]);
eq = tor_W_ful(3) + tor_V_ful(3) + tor_R_ful(3) == 0;

solve(subs(eq, [pos_W_left_x, pos_ful_left_x], [0.5, 1.25]))
```

ans =
$`\displaystyle 140`$

(b)

``` matlab
eval(solve(subs(eq, [wei_W, pos_W_left_x], [140, 0.5 + 0.25])))
```

``` matlabTextOutput
ans = 1.3459
```
