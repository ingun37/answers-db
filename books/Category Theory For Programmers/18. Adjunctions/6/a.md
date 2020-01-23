We are asked to define Exponential in Haskell.  
FYI, it's not mentioned in the book but the Exponential that is described in the book is basically currying.  

```haskell
unit z a = (z, a)
counit (f, a) = f a
```