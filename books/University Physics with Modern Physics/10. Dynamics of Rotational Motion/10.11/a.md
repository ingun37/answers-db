```matlab
m=0.225
R=0.03/2
F=[0;-0.02]
I=2/5*m*R^2
tau = cro2([R;0],F)
alpha = tau / I
answer('a',alpha)
answer('b',22.5/alpha)
```