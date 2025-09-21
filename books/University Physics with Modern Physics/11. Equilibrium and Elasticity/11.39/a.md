``` matlab
clear;
syms Rs Ts S Ta;
As = Rs ^ 2 * pi;
Ms = Ts / As / S;
Aa = (2*Rs) ^ 2 * pi;
Ma = Ta / Aa / S;
solution = solve(Ms / Ma == 20e10 / 7e10, Ta)
```

solution =
$`\displaystyle \frac{7\,\textrm{Ts}}{5}`$
