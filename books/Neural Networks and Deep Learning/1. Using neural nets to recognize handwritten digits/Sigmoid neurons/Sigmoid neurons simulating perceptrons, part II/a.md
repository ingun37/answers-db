In the previous problem it's proven that multiplying a scalar to weight and bias vectors doesn't change the output of perceptrons.

For sigmoid neurons however,

```math
\begin{aligned}
& \lim\limits_{c \rightarrow \infin} \frac{1}{1+\exp(- c w \cdot x- cb)} \\
&= \lim\limits_{c \rightarrow \infin} \frac{1}{1+\exp(-c(w \cdot x + b))} \\
&= \lim\limits_{c \rightarrow \infin} \frac{1}{1+\exp^{-c}(w \cdot x + b)} \\
&= \begin{cases}
   0 &\text{if } w \cdot x + b < 0 \\
   1 &\text{if } w \cdot x + b > 0
\end{cases}
\end{aligned}
```

which is exactly the definition of perceptron.

If $`w \cdot x + b = 0`$ then

```math
\frac{1}{1+e^{-0c}} = \frac{1}{1+1} = {1 \over 2}
```

which is not a possible outcome of perceptron.