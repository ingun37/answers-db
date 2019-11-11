Show the isomorphism between the standard definition of Maybe and this desugaring:
```haskell
type Maybe' a = Either (Const () a) (Identity a)
```
Hint: Define two mappings between the two implementations. For additional credit, show that they are the inverse of each other using equational reasoning.