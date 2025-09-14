```matlab
clear;
r = 0.65/2;
S = 0.2 * 2; % shaft length
M = 8;
w = [ 5 * 2 * pi ;
      0          ;
      0         ];
g = 9.8;
I = M * r^2;
L = I * w;
```
(a)
```matlab
holding_weight = [0;M*g;0];

holding_force = [holding_weight/2 holding_weight/2];


disp('holding force')
disp(holding_force)
```
```
         0         0
   39.2000   39.2000
         0         0
```
(b)
```matlab
function rotation = calc_rotation_force(shaft_rev_per_sec, L, S)
syms t
ws = shaft_rev_per_sec * 2 * pi;

Lt = norm(L) * [cos(ws * t); 0; -sin(ws * t)];
Tt = diff(Lt, t);
T0 = subs(Tt, t, 0);
syms F
syms Fr [3 1]
Fl = -Fr;
right_torque = cross([-S/2;0;0], Fr);
left_torque = cross([S/2;0;0],Fl);
Fr0=solve(right_torque + left_torque == T0, Fr);
rotation.right = [Fr0.Fr1;Fr0.Fr2;Fr0.Fr3];
rotation.left = -rotation.right;
rotation = [rotation.left rotation.right];
end

disp('when shaft rev is 0.05')
disp(eval(holding_force + calc_rotation_force(0.05, L, S)))
```
```
         0         0
   18.3505   60.0495
         0         0
```
(c)
```matlab
disp('when shaft rev is 0.3')
disp(eval(holding_force + calc_rotation_force(0.3, L, S)))
```
```
         0         0
  -85.8972  164.2972
         0         0
```
(d)
```matlab
syms x
m = holding_force + calc_rotation_force(x, L, S)
eval(solve(m(2,1)==0,x))
```
```
ans = 0.0940
```