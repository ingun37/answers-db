```haskell
{-# LANGUAGE TypeFamilies #-}

import Data.Functor
import Data.Functor.Contravariant

class Representable f where
    type Rep f :: *
    tabulate :: (Rep f -> x) -> f x 
    index :: f x -> Rep f -> x

data Stream x = Cons x (Stream x)

instance Representable Stream where
    type Rep Stream = Int
    tabulate f = Cons (f 0) (tabulate (f . (+1)))
    index (Cons b bs) n = if n == 0 then b else index bs (n - 1)

indexStream :: Stream x -> Int -> x
indexStream = index
squared :: Int -> Int
squared = indexStream (tabulate (^2))

memoize :: (Int -> a) -> (Int -> a)
memoize f = (map f [0 ..] !!)

sqMemo = memoize squared

main :: IO ()
main = print $ sqMemo 10
```