Let `A` be a `fromY` function to which `B` is mapped.
Let `B'` be the `A id` in other words `B'` is `btoa` function to which `A` is mapped.
Now let `A'` be the `fromY` function to which `B'` is mapped. `A'` must be same to `A` if it's isomorphic.
```haskell
A' f b = f (B' b)
= f (A id b)
= f (id B b)
= f (B b)
```
It says `A'` is also mapped from `B` which means `B = B'` which means `A = A'`
