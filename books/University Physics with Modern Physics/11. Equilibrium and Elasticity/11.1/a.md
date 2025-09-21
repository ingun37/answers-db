``` matlab
M=0.12;
L=0.5;
ml = 0.055;
mr = 0.11;
l=0;
m=L/2;
r=L;
dot([ml;M;mr],[l,m,r])/(M+ml+mr)
```

``` matlabTextOutput
ans = 0.2982
```
