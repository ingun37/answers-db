```haskell
module Rib
    ( coalg, toListC
    ) where
import Data.Fix
import Data.Matrix

data StreamF a = StreamF Int a

instance Functor StreamF where
    fmap f (StreamF n x) = StreamF n (f x)

type Stream = Fix StreamF

coalg :: Int -> StreamF Int
coalg n = StreamF (n*n) (n+1)

toListC :: Fix StreamF -> [Int]
toListC = cata al where al :: StreamF [Int] -> [Int]
                        al (StreamF n arr) = n : arr
```
## Test
```haskell
import Rib
import Data.Fix

main :: IO ()
main = do
    print $` take 5 `$ toListC $ ana coalg 1
```
## Result
```shell
ingun$ stack test
...
[1,4,9,16,25]
```