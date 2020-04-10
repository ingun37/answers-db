```haskell
module Lib
    ( alg, RingF(..), calc
    ) where
import Data.Fix

data RingF a = RZero
             | ROne
             | RAdd a a 
             | RMul a a
             | RNeg a

instance Functor RingF where
    fmap f r = case r of
        RZero -> RZero
        ROne -> ROne
        RAdd a b -> RAdd (f a) (f b)
        RMul a b -> RMul (f a) (f b)
        RNeg a -> RNeg (f a)

type Ring = Fix RingF

take' :: Int -> [Int] -> [Int]
take' n l = if n > 0 then case l of [] -> replicate n 0
                                    (x:xs) -> x:(take' (n-1) xs)
                     else []
degree :: [Int] -> Int
degree xs = max 0 $ length xs - 1

alg :: RingF [Int] -> [Int]
alg RZero = []
alg ROne = [1]
alg (RNeg x) = map negate x
alg (RAdd (x:xs) (y:ys)) = (x+y):(alg $ RAdd xs ys)
alg (RAdd [] y) = y
alg (RAdd x []) = x
alg (RMul x y) = let f :: Int -> Int
                     f n = let xs = take' (n+1) x
                               ys = reverse $ take' (n+1) y in
                                   sum $ zipWith (*) xs ys
                     in
                         map f [0..(degree x + degree y)]

```

## Test

```haskell
import Lib
import Data.Fix

main :: IO ()
main = do
    print $` cata alg `$ Fix (RAdd (Fix ROne) (Fix ROne))
```

## Result
```shell
ingun$ stack test
...
[2]
```