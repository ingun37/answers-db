```matlab
clear;
spilled = 3.78541 * 0.001; % in cubic meter
D_tank = 3; % in m
```

(a)

```matlab
syms s_tank
A_tank = (D_tank/2)^2*pi;
s_tank = double(solve(s_tank * A_tank == spilled))
```

```matlabTextOutput
s_tank = 5.3553e-04
```

(b)

```matlab
syms s_stream  t positive
D_stream = 0.5e-2;
A_stream = (D_stream/2)^2*pi
```

```matlabTextOutput
A_stream = 1.9635e-05
```

```matlab
s_stream = double(solve(s_stream * A_stream == spilled));


atm = 1.013e5;
g = -9.8;
h = -2;


v = sqrt(2*g*h);
double(solve(spilled / t == A_stream * v))
```

```matlabTextOutput
ans = 30.7921
```