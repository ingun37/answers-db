Show that the following data types define bifunctors in `a` and `b`:
```haskell
data K2 c a b = K2 c
data Fst a b = Fst a
data Snd a b = Snd b
```
For additional credit, check your solutions agains Conor McBride’s paper [Clowns to the Left of me, Jokers to the Right](http://strictlypositive.org/CJ.pdf).