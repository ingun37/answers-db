```matlab
clear;
diameter=42/100;
radius = diameter/2;
syms density
circum = pi * diameter;
Mr = circum * density;

% length of spoke
L = radius;

% Moment of Inertia of rim
Ir = Mr * radius ^ 2;

% mass of a spoke
Ms = L * density;

% Moment of Inertia of a spoke
Is = 1/3 * Ms * L^2;

m = Mr + Ms * 6;
I = Ir + Is * 6;
h=58;
g=9.8;
syms v
rotationEnergy = 1/2 * I * (v/radius)^2;
translatEnergy = 1/2 * m * v^2;
eq0 = m*g*h == rotationEnergy + translatEnergy
eval(solve(eq0, v, Real=true))
```