```matlab
clear;
g=-9.8;
Wp = -80;
Mp = Wp / g;
Wx = -75;
Wy = -125;
r=0.3;
I = 1/2 * Mp * r^2;
syms Tx Ty a
e1 = Wx + Tx == Wx/g * a
e2 = Wy + Ty == Wy/g * -a
e3 = Tx*r - Ty*r == I * -a/r
sol = solve([e1, e2, e3], [Tx, Ty, a])
eval(-sol.Tx - sol.Ty + Wp)
```