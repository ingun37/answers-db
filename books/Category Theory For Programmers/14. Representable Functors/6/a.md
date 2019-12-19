```haskell
data Pair a = Pair a a
instance Representable Pair where
    type Rep Pair = Bool
    tabulate f = Pair (f True) (f False)
    index (Pair x y) = \b -> if b then x else y
```