```matlab
clear;
syms m_coin m_block h A;
g = 9.8;
W_coin = -m_coin * g;
W_block = -m_block * g;
buoy = h * A * 1e3 * g;
eq1 = W_coin + W_block + buoy == 0;
eq2 = W_block + subs(buoy, h, 0.0312) == 0;


sol = solve([eq1 eq2], [m_block, h])
```

```matlabTextOutput
sol = struct with fields:
    m_block: (156*A)/5
          h: (156*A + 5*m_coin)/(5000*A)


```

```matlab


% using the slope from the sol.h
A_sol = solve(5 / (5000 * A) == 0.039)
```

A_sol = 
 $\displaystyle \frac{1}{39}$
 

```matlab
m_block = subs(sol.m_block, A, A_sol)
```

m_block = 
 $\displaystyle \frac{4}{5}$