let `psi’ fa = (flip fmap) fa` so `psi` and `phi`‘s each input/output type match. (flip swaps the order of parameters)

```haskell
phi (psi’ fa)
= (psi’ fa) id
= ((flip fmap) fa) id
= fmap id fa
= fa
```