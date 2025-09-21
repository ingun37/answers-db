``` matlab
clear;
A=0.5/100;
L = 4;
elongation = 0.2/(100^2);
F=5000;
tensile_stress = F / A;
tensile_strain = elongation / L;
tensile_stress / tensile_strain
```

``` matlabTextOutput
ans = 2.0000e+11
```
