Following code is same implementation as http://strictlypositive.org/CJ.pdf (the referenced paper from the question.)
```haskell
data K2 c a b = K2 c
data Fst a b = Fst a
data Snd a b = Snd b

instance Bifunctor (K2 c) where
    bimap f g (K2 c) = K2 c
instance Bifunctor Fst where
    bimap f g (Fst a) = Fst (f a)
instance Bifunctor Snd where
    bimap f g (Snd b) = Snd (g b)
```