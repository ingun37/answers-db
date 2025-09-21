``` matlab
glycerin_comp = 21e-6;
ethyl_comp = 111e-6;
syms stress_g strain stress_e
solve([
    glycerin_comp / ethyl_comp == (-strain/stress_g) / (-strain/stress_e)
    ], stress_e)
```

ans =
$`\displaystyle \frac{7\,{\textrm{stress}}_g }{37}`$

``` matlab
7/37
```

``` matlabTextOutput
ans = 0.1892
```
