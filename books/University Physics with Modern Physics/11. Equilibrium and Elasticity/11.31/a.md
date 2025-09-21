``` matlab
strain = -0.5 / 100;
modulus = 4.1e10;
syms stress
eq = modulus == -stress/strain;
in_pascal = solve(eq)
```

in\_pascal =
$`\displaystyle 205000000`$

``` matlab
eval(in_pascal/1.013e5)
```

``` matlabTextOutput
ans = 2.0237e+03
```
