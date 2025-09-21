``` matlab
clear;
syms alpha
Wy = -1
```

``` matlabTextOutput
Wy = -1
```

``` matlab
AA = 2;
AB = 4;
FAy = -Wy * (1-alpha);
FBy = -Wy * alpha;
alpha_equal_stress = solve(FAy / AA == FBy / AB)
```

alpha\_equal\_stress =
$`\displaystyle \frac{2}{3}`$

(a)

``` matlab
eval(alpha_equal_stress * 1.05)
```

``` matlabTextOutput
ans = 0.7000
```

(b)

``` matlab
YA = 1.8e11;
YB = 1.2e11;
SA = FAy/AA/YA;
SB = FBy/AB/YB;
alpha_equal_strain = solve(SA == SB);
eval(alpha_equal_strain * 1.05)
```

``` matlabTextOutput
ans = 0.6000
```
