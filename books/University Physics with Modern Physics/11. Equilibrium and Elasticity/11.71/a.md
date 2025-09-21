``` matlab
syms Ay By
w = 1.25;
h = 0.5;

alpha = (w-h)/2 / w;
beta = ((w-h)/2 + h )/w;
sum = alpha + beta;
Ay = 9.8 * 200 * alpha / sum
```

``` matlabTextOutput
Ay = 588
```

``` matlab
By = 9.8 * 200 * beta / sum
```

``` matlabTextOutput
By = 1372
```
