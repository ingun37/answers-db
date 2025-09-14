```matlab
clear;
function y=moment_of_inertia(r)
  syms Icm m
  y=Icm + m*r^2;
end
syms r1 v1 r v
I1 = moment_of_inertia(r1);
I = moment_of_inertia(r);
w1 = v1/r1;
w = v/r;
angular_momentum_conservation = I1*w1 == I*w;
v = solve(angular_momentum_conservation, v)

a = v ^ 2 / r;
syms m Icm
T = m * a;
```
(a)
```matlab
T=subs(T, Icm, 0)
```
```math
\frac{m\,{r_1 }^2 \,{v_1 }^2 }{r^3 }
```
(b)
```matlab
syms r1 r2
W = int(T, r, r1, r2)
```
```math
\left\lbrace \begin{array}{cl}
m\,{r_1 }^2 \,{v_1 }^2 \,\int_{r_1 }^{r_2 } \frac{1}{r^3 }\;\textrm{d}r & \;\textrm{if}\;\;r_1 \le 0\wedge 0\le r_2 \\
m\,{r_1 }^2 \,{v_1 }^2 \,{\left(\frac{1}{2\,{r_1 }^2 }-\frac{1}{2\,{r_2 }^2 }\right)} & \;\textrm{if}\;\;0<r_1 \vee r_2 <0
\end{array}\right.
```
(c)
```matlab
function y=kinetic_energy(r,v)
  y=1/2 * moment_of_inertia(r) * (v/r)^2;
end

K1 = kinetic_energy(r1, v1);

K2 = kinetic_energy(r2, subs(v, r, r2));
subs(K2-K1, [Icm], [0])
```

```math
\frac{m\,{r_1 }^2 \,{v_1 }^2 }{2\,{r_2 }^2 }-\frac{m\,{v_1 }^2 }{2}
```