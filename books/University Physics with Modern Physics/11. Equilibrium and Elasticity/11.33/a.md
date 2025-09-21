(a)

``` matlab
clear;
syms stress
strain = 0.1/100;
modulus = stress / strain;
atm = 1.013e5;
Gpa = 1000^3;
stress = eval(solve(modulus == 15*Gpa)/atm)
```

``` matlabTextOutput
stress = 148.0750
```

(b)

``` matlab
stress * atm / 10000
```

``` matlabTextOutput
ans = 1500
```
