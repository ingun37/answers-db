```haskell
data Pair a b = Pair a b

instance Bifunctor Pair where
  bimap f g (Pair a b) = Pair (f a) (g b) 
  -- = first f (Pair a (g b))
  -- = first f (second g (Pair a b))
  -- = first f . second g (Pair a b)
  first f (Pair a b) = Pair (f a) b
  -- = Pair (f a) (id b)
  -- = bimap f id (Pair a b)
  second g (Pair a b) = Pair a (g b)
  -- = Pair (id a) (g b)
  -- = bimap id g (Pair a b)
```