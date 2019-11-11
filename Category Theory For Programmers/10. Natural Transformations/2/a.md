```haskell
data Reader a b = Reader (a -> b)
nt1 :: Reader () a -> [a]
nt1 (Reader f) = [f ()]
nt2 :: Reader () a -> [a]
nt2 _ = []
nt3 :: Reader () a -> [a]
nt3 (Reader f) = f () : nt3 (Reader f)
```