```haskell
nt :: Maybe a -> [a]
nt Nothing = []
nt (Just a) = [a]
-- fmap f (nt Nothing) = fmap f [] = []
-- fmap f (nt Just a) = fmap f [a] = [b]
-- nt fmap f Nothing = nt Nothing = []
-- nt fmap f (Just a) = nt (Just b) = [b]
```