Let $`S`$ be the event that an email is a spam, $`W`$ that an email contains the word.
We are asked to calculate $`P(S|W)`$. Using Bayes' rule we can turn it into:

```math
\cfrac{P(W|S)P(S)}{P(W)}
```

Using the law of total probability, we can further turn it into:

```math
\cfrac{P(W|S)P(S)}{P(W|S)P(S) + P(W|S^c)P(S^c)}
```

Substituting what we can with what we are given:

```math
\cfrac{0.01*0.5}{0.01*0.5 + 0.00001*0.5} \approx 0.999
```