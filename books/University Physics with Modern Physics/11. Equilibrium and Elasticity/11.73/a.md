``` matlab
clear;
syms T_max h D L
```

(a) from observation

``` matlab
w_max = T_max * h * D / (L * sqrt(D^2 + L^2))
```

w\_max =
$`\displaystyle \frac{\textrm{D}\,T_{\max } \,h}{L\,\sqrt{{\textrm{D}}^2 +L^2 }}`$

(b)

``` matlab
derivation = diff(w_max, D);
simp = subs(derivation, [T_max, h, L], [1, 1, 1]);
x = 0:pi/10:2*pi;
y = subs(simp, x);
plot(x,y)
```

\!\[figure\_0.png\](./chapter 11\_media/figure\_0.png)

so it's positive
