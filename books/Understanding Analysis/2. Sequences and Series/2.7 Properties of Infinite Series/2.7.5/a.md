Say $`(h_n) = 1/n^p`$.

I'm using Cauchy Condensation Test.

```math
\begin{aligned}
  & h_1 + 2h_2 + 4h_4 + \cdots + 2^k b_{2^k} \\
= & \frac 1 {1^p} + \frac 2 {2^p} + \frac 4 {4^p} + \cdots + \frac {2^k} {2^{kp}}\\
= & \frac 1 {1^p} + \frac 2 {2^p} + \frac {2^2} {2^{2p}} + \cdots + \frac {2^k} {2^{kp}} \\
= & \frac 1 {1^p} + \frac 1 {2^{p-1}} + \frac {1} {2^{2p-2}} + \cdots + \frac {1} {2^{kp - k}} \\
= & \frac 1 {1^p} + \frac 1 {2^{p-1}} + \frac {1} {(2^{p-1})^2} + \cdots + \frac {1} {(2^{p-1})^k} \\
\end{aligned}
```

This is geometric series of $`\frac {1} {2^{p-1}}`$.

Therefore if $`1 < p`$ then it converges, otherwise it diverges.