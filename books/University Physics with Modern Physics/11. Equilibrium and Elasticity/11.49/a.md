(a)

``` matlab
clear;
syms Tx Ty Px Py
Wy = -82 * 9.8;
W = [0;Wy];
T = [Tx;Ty];
P = [Px;Py];
theta = deg2rad(35);

body_dir_pivot = [cos(theta);sin(theta)];
clip_len_pivot = 1.4;
clip_pivot = body_dir_pivot * clip_len_pivot;
torq_T_pivot = cross([clip_pivot;0],[T;0]);
cm_len_pivot = 1.1;
cm_pivot = body_dir_pivot * cm_len_pivot;
torq_W_pivot = cross([cm_pivot;0],[W;0]);

clip_cm = clip_pivot - cm_pivot;
torq_T_cm = cross([clip_cm;0],[T;0]);
pivot_cm = -cm_pivot;
torq_P_cm = cross([pivot_cm;0],[P;0]);

cm_clip = -clip_cm;
torq_W_clip = cross([cm_clip;0],[W;0]);
pivot_clip = -clip_pivot;
torq_P_clip = cross([pivot_clip;0],[P;0]);

head_len_pivot = 1.9;
head_pivot = body_dir_pivot * head_len_pivot;
clip_head = clip_pivot - head_pivot;
torq_T_head = cross([clip_head;0],[T;0]);
cm_head = cm_pivot - head_pivot;
torq_W_head = cross([cm_head;0],[W;0]);
pivot_head = -head_pivot;
torq_P_head = cross([pivot_head;0],[P;0]);

tau = pi/2 - theta;
phi = deg2rad(25);
psi = pi - tau - phi;
syms H
H = eval(solve(sin(phi)/1.4 == sin(psi)/H))
```

``` matlabTextOutput
H = 3.2624
```

``` matlab
syms K
K = eval(solve(sin(tau)/K == sin(phi)/1.4))
```

``` matlabTextOutput
K = 2.7136
```

``` matlab

pivot_fix = [0;-H];
torq_P_fix = cross([pivot_fix;0],[P;0]);
clip_fix = K*[cos(-(pi/2-phi));sin(-(pi/2-phi))];

cm_fix = pivot_fix * (0.3/1.4) + clip_fix * (1.1/1.4);
torq_W_fix = cross([cm_fix;0],[W;0]);

solution = solve([
    Px + Tx == 0,
    Py + Ty + Wy == 0,
    %torq_T_head(3) + torq_W_head(3) + torq_P_head(3) == 0,
    torq_T_pivot(3) + torq_W_pivot(3) == 0,
    %torq_T_cm(3) + torq_P_cm(3) == 0,
    %torq_W_clip(3) + torq_P_clip(3) == 0,
    torq_P_fix(3) + torq_W_fix(3) == 0
    ])
```

``` matlabTextOutput
solution = struct with fields:
    Px: 815261466625336064/3673085336942935
    Py: 6215084043552808843881817103431102/18970699644194571873317849059795
    Tx: -815261466625336064/3673085336942935
    Ty: 1805954038104389822703281280204032/3794139928838914374663569811959

```

``` matlab

eval(norm([solution.Tx, solution.Ty]))
```

``` matlabTextOutput
ans = 525.1914
```

(b)

``` matlab
eval([solution.Px, solution.Py])
```

``` matlabTextOutput
ans = 1x2
  221.9555  327.6149

```

(c)

``` matlab
eval(solution.Py/solution.Px)
```

``` matlabTextOutput
ans = 1.4760
```
