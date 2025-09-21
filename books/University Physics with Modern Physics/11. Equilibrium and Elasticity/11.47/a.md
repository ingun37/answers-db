``` matlab
clear;
cg = [1/2;0];
w = [0;-25];
T1 = cross([cg;0],[w;0])
```

``` matlabTextOutput
T1 = 3x1
         0
         0
  -12.5000

```

``` matlab
syms W x
x0 = -1;
x1 = -1/4;
exp = -W*x/(x1-x0);
T2z = int(exp,x,[x0,x1])
```

T2z =
$`\displaystyle \frac{5\,W}{8}`$

``` matlab
% T2z = 1/2 * (W / (x1 - x0)) * (x0^2 - x1^2)
solve(T1(3) == T2z)
```

ans =
$`\displaystyle -20`$
