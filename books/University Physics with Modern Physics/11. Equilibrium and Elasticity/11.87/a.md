``` matlab
clear;
p = 1.5;
cg = 1.88 - p;
P1 = 0.2 - p;
syms M x m2
P2 = x - p;
g = -9.8;
m1 = 2;
net_torq = torque([P1;0],[0;m1*g]) + torque([P2;0],[0;m2*g]) + torque([cg;0],[0;M*g]);
```

(b)

``` matlab
x_in_terms_of_m2 = solve(net_torq == 0, x)
```

x\_in\_terms\_of\_m2 =
$`\displaystyle \frac{75\,m_2 -19\,M+130}{50\,m_2 }`$

(c)

``` matlab
x_sample = [3.5, 2.83, 2.50, 2.32, 2.16, 2.00];
m2_sample = [1.00, 1.50, 2.00, 2.50, 3.00, 4.00];
m2_inv_sample = 1 ./ m2_sample;
B = mldivide(transpose(m2_inv_sample), transpose(x_sample - 1.5));
plot(m2_inv_sample, x_sample, m2_inv_sample, m2_inv_sample .* B + 1.5);
```

\!\[figure\_1.png\](./chapter 11\_media/figure\_1.png)

``` matlab
eval(solve(B == (130 - 19*M)/50))
```

``` matlabTextOutput
ans = 1.5743
```

(c)

``` matlab
1.5
```

``` matlabTextOutput
ans = 1.5000
```
