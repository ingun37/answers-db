``` matlab
clear;
Fmag = 8;
syms l
F1 = [0;Fmag];
F2 = [0;-Fmag];
torqF1 = cross([3;0;0],[F1;0]);
torqF2 = cross([3+l;0;0],[F2;0]);
eqT = torqF1(3) + torqF2(3) == -6.4;
eval(solve(eqT, l))
```

``` matlabTextOutput
ans = 0.8000
```
