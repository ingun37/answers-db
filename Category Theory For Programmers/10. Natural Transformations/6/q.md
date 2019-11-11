Create a few test cases for the opposite naturality condition of transformations between different `Op` functors. Here’s one choice:
```haskell
op :: Op Bool Int
op = Op (\x -> x > 0)
```
and
```haskell
f :: String -> Int
f x = read x
```