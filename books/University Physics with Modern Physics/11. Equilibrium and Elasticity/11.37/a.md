``` matlab
clear;
F=9e5;
thickness = 0.5e-2;
side = 10e-2;
A=side * thickness;
h=side;
modulus = 7.5e10;
syms x
x=eval(solve(modulus == F/A/(x/h)));
```

(a)

``` matlab
x/h
```

``` matlabTextOutput
ans = 0.0240
```

(b)

``` matlab
x * 100
```

``` matlabTextOutput
ans = 0.2400
```
