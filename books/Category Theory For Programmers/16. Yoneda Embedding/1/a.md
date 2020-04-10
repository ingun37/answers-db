It's asking to express following statement.

forall x, (x -> a) -> (x -> b) $`\cong`$ a -> b

When the book was explaining yoneda embedding, it uncurried only the last `b`.  
But this time we will uncurry the whole `C(x, b)` part, which is the last two `x -> b`. And also we will name the right hand side as `atob`
```haskell
fromY :: (x -> a) -> (x -> b)
fromY f -> atob . f
```
And the conversion is same.
```haskell
fromY id :: a -> b
```