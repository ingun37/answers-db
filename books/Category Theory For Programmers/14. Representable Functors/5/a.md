```haskell
(index . tabulate f) 0
= index (Cons (f 0) (tabulate (f . (+1)))) 0
= f 0
(index . tabulate f) n+1
= index (Cons (f 0) (tabulate (f . (+1)))) n+1
= index (tabulate (f . (+1))) (n)
= index . tabulate g n
= g n
= f . (+1) n
= f n+1
```