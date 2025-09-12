```matlab
clear
m=2;
v=[12;0];
p=rotd(180-36.9) * [8;0];
```
(a)
```matlab
cro2(p, m*v)
```
(b)
```matlab
cro2(p, [0;-m * 9.8])
```