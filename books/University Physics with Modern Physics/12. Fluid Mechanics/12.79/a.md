```matlab
clear;


D0 = 1.8e-2;
A0 = (D0/2)^2*pi;
D1 = 0.75e-2;
A1 = (D1/2)^2*pi;
0.95*(A0/A1) % Because A0*v0 == A1*v1
```

```matlabTextOutput
ans = 5.4720
```