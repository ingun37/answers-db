``` matlab
clear;
syms lx Xy
A = [0  ;  500; 0];
B = [0  ;  400; 0];
W = [0  ; -350; 0];
L = [1.5;  0  ; 0];
l = [lx ;  0  ; 0];
X = [0  ;  Xy ; 0];

torq0 = cross(L/2, W);
torq1 = cross(l, X);
torq2 = cross(L, B);

eq0 = A(2) + W(2) + X(2) + B(2) == 0;
eq1 = torq0(3) + torq1(3) + torq2(3) == 0;

solution = solve([eq0 eq1], [lx Xy]);
eval(solution.lx)
```

``` matlabTextOutput
ans = 0.6136
```

``` matlab
eval(solution.Xy)
```

``` matlabTextOutput
ans = -550
```
