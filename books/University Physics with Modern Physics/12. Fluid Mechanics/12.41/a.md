```matlab
clear;
A = 0.15^2*pi;
throughput = 1.2;
syms v
```

(a)

```matlab
double(solve(throughput == A*v))
```

```matlabTextOutput
ans = 16.9765
```

(b)

```matlab
v = 3.8;
syms r positive
double(solve(throughput == (r^2*pi)*v))
```

```matlabTextOutput
ans = 0.3170
```