```matlab
clear;
syms p0 positive
% p0 = 5e3; % pressure of compressed air
p1 = 0; % air pressure
rho_h2o = 1e3;
g = 9.8;


syms v h positive
potential_energy = p0 + rho_h2o*g*h;
kinetic_energy = p1 + 0.5*rho_h2o*v^2;
```

(a)

```matlab
% can't use Torricelli's law because it's not regular air pressure
v = solve(potential_energy == kinetic_energy)
```

v = 
 $\displaystyle \frac{\sqrt{5}\,\sqrt{9800\,h+p_0 }}{50}$
 

```matlab
closed = double(subs(v, [h, p0], [0.8, 5e3]))
```

```matlabTextOutput
closed = 5.0675
```

```matlab
open = double(subs(v, [h, p0], [0.8, 0]))
```

```matlabTextOutput
open = 3.9598
```

```matlab
ratio = closed/open
```

```matlabTextOutput
ratio = 1.2797
```

(b)

```matlab
function out=f(p0)
r1 = 0.02/2;
A1 = r1^2*pi;
r0 = 2/2;
A0 = r0^2*pi;
syms t h
h_prime = 9800*h+p0;
lhs = -A0 * int(1/sqrt(h_prime), h, [0.8 0]);
rhs = sqrt(5)/50*A1*t;
seconds = double(solve(lhs == rhs));
out=seconds;
end
seconds_closed = f(5e3);
minutes_closed = seconds_closed/60
```

```matlabTextOutput
minutes_closed = 32.4025
```

```matlab


seconds_open = f(0);
ratio = seconds_open/seconds_closed
```

```matlabTextOutput
ratio = 2.0783
```