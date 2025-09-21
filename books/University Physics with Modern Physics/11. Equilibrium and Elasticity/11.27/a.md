``` matlab
clear;
syms D
A = (D/2)^2*pi;
force_each = 700;
tensile_stress = force_each / A;
tensile_strain = 0.25 / 100 / 2;
Y = tensile_stress / tensile_strain;
solution = solve(Y == 2.0e11)
```

solution =

``` math
\displaystyle \left(\begin{array}{c} -\frac{\sqrt{7}\,\sqrt{156250}}{312500\,\sqrt{\pi }}\newline \frac{\sqrt{7}\,\sqrt{156250}}{312500\,\sqrt{\pi }} \end{array}\right)
```

``` matlab
eval(solution(2))
```

``` matlabTextOutput
ans = 0.0019
```
