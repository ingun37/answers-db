Show that the two functions `phi` and `psi` that form the Yoneda isomorphism in Haskell are inverses of each other.

```haskell
phi :: (forall x . (a -> x) -> F x) -> F a
phi alpha = alpha id
```

```haskell
psi :: F a -> (forall x . (a -> x) -> F x)
psi fa h = fmap h fa
```