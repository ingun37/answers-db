```matlab
clear;
% use Torricelli's law
syms h g R H positive
v=sqrt(2*g*h);
t = R / v; % traveling time
```

(a)

```matlab
eq = (H-h) == (1/2) * g * t^2;
cond = h < H;
R_ = solve([eq, cond], R)
```

```matlabTextOutput
Warning: Solutions are only valid under certain conditions. To include parameters and conditions in the solution, specify the 'ReturnConditions' value as 'true'.
```

R_ = 
 $\displaystyle 2\,\sqrt{h}\,\sqrt{H-h}$
 

(b)

```matlab
syms h2 positive % from the bottom
R__ = subs(R_, h, (H-h2))
```

R__ = 
 $\displaystyle 2\,\sqrt{h_2 }\,\sqrt{H-h_2 }$
 

```matlab
solve(R_ == R__, h2)
```

```matlabTextOutput
Warning: Possibly spurious solutions.
Warning: Solutions are only valid under certain conditions. To include parameters and conditions in the solution, specify the 'ReturnConditions' value as 'true'.
```

ans = 

  $$ \displaystyle \left(\begin{array}{c} h\newline H-h \end{array}\right) $$