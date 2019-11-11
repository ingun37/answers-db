```haskell
data Reader a b = Reader (a -> b)

rb1 :: Reader Bool a -> [a]
rb1 (Reader f) = [f True]
rb2 :: Reader Bool a -> [a]
rb2 _ = []
rb3 :: Reader Bool a -> [a]
rb3 (Reader f) = f False : rb3 (Reader f)

m1 :: Maybe a -> [a]
m1 (Just a) = [a]
m1 Nothing = []
m2 :: Maybe a -> [a]
m2 _ = []
m3 :: Maybe a -> [a]
m3 (Just a) = a : m3 (Just a)
m3 Nothing = []
```