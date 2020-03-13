Let's try another data structure. I call it a `PreList` because it's a precursor to a `List`. It replaces recursion with a type parameter `b`.
```haskell
data PreList a b = Nil | Cons a b
```
You could recover our earlier definition of a `List` by recursively applying `PreList` to itself (we'll see how it's done when we talk about fixed points).
Show that `PreList` is an instance of Bifunctor.