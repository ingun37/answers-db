```matlab
clear;
syms L R r positive;
dP = L / R^4;
double(solve(dP == 2*L / (r*R)^4, r))
```

```matlabTextOutput
ans = 1.1892
```