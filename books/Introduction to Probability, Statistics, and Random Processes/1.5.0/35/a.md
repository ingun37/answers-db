The game starts with either *H* or *T*. Therefore there are only two patterns for the game to end with *HH*.

| Start with *H* | Start with *T* |
| -------------- | -------------- |
| HH | THH |
| HT HH | TH THH |
| HT HT HH | TH TH THH |
| ... | ... |

The probability for each can be calculated by using geometric sum. Let $`P_h`$ be the probability of starting with *H*, $`P_t`$ the *T*.

```math
P_h = \dfrac{pp}{1-pq} \\
\text{ } \\
P_t = \dfrac{qpp}{1-qp}
```

Therefore the answer is

```math
\cfrac{\cfrac{pp}{1-pq}}{\cfrac{pp}{1-pq} + \cfrac{qpp}{1-qp}} = \cfrac{pp}{pp + qpp}
```