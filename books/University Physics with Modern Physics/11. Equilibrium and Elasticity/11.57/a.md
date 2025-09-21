(a)

``` matlab
clear;
% solved by hand
syms m g T L
theta = atan(m * g / (2*T))
```

theta =
$`\displaystyle \textrm{atan}\left(\frac{g\,m}{2\,T}\right)`$

(b)

``` matlab
% solved by hand
% use that integral of torque is the energy and energy is moment of inertia
% angular speed squared
% times
clear;
syms g theta L
w = sqrt(3 * g * sin(theta) / L)
```

w =
$`\displaystyle \sqrt{3}\,\sqrt{\frac{g\,\sin \left(\theta \right)}{L}}`$
