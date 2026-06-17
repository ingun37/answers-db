```matlab
clear;
syms v h positive
m = 1; % arbitrary mass
g=9.8;


initial_kinetic_energy = (1/2) * m * v^2;
final_potential_energy = m*g*h;


energy_conservation_eq = initial_kinetic_energy == final_potential_energy;


throughput = 0.5;


syms r positive
A = r^2*pi;


throughput_eq = A*v == throughput;


sol = solve([energy_conservation_eq throughput_eq]);
```

(a)

```matlab
D = 2*double(subs(sol.r, h, 28))
```

```matlabTextOutput
D = 0.1648
```

(b)

```matlab
sol = solve([energy_conservation_eq subs(throughput_eq, r, D)], [h v]);
double(sol.h)
```

```matlabTextOutput
ans = 1.7500
```