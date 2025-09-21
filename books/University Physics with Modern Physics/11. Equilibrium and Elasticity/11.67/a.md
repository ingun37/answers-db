``` matlab
clear;
len_low = 0.9;
len_upper = 0.75 + 0.6;

% angle between foot and floor
theta = atan(len_upper/len_low);

lc = (len_low - 0.41) * [cos(theta); sin(theta)];
phi = pi/2 + theta;
B = norm([len_low;len_upper]);
uc =[B;0] + (len_upper - 0.65) * [cos(phi);sin(phi)];
LW = [0;-277];
UW = [0;-473];
tor_LW = cross([lc;0],[LW;0]);
tor_UW = cross([uc;0],[UW;0]);

syms FNy HNy
tor_HN = cross([B;0;0],[0;HNy;0]);
sol = solve([ ...
    LW(2) + UW(2) + FNy + HNy == 0, ...
    tor_LW(3) + tor_UW(3) + tor_HN(3) == 0
    ]);
```

(a)

``` matlab
normal_force_one_hand = eval(sol.HNy/2)
```

``` matlabTextOutput
normal_force_one_hand = 174.8043
```

``` matlab
normal_force_one_foot = eval(sol.FNy/2)
```

``` matlabTextOutput
normal_force_one_foot = 200.1957
```

(b)

``` matlab
syms FFx
hip_from_foot = len_low * [cos(theta); sin(theta)];
foot_from_hip = -hip_from_foot;
tor_FF = cross([foot_from_hip;0],[FFx;0;0]);
tor_FN = cross([foot_from_hip;0],[0;2*normal_force_one_foot;0]);
tor_LW_from_hip = cross([lc - hip_from_foot;0],[0;-277;0]);
FFx = solve(tor_FF(3)+tor_FN(3)+tor_LW_from_hip(3) == 0);

friction_one_hand = eval(FFx/2)
```

``` matlabTextOutput
friction_one_hand = 91.4009
```
