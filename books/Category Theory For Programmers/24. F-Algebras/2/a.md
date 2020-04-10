Just like the book represented univariate polynomial with 1d array, I represented multivariate polynomial with multi-dimension array. But the data structure for multi-dimension array is just a function. The function accepts index value of `[Int]`. You can think of each element represents degree of `x, y, z ...`s. For example, `[0,1,2]` will mean $`x^0y^1z^2`$ (simply $`yz^2`$) and the function will return it's coefficient.

Interesting thing is I used another F-Algebra `Pair`. It's just like the `StreamF` from the book which is used to demonstrate a conversion to List.

```haskell
module NPoly
    ( bb, alg, NPoly, mulPoly
    ) where
import Data.Fix
import Data.Bifunctor

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

type NPoly = [Int] -> Int

alg :: RingF NPoly -> NPoly
alg RZero = const 0
alg ROne = \x -> if all (0==) x then 1 else 0
alg (RAdd f g) = \x -> (f x) + (g x)
alg (RMul f1 f2) = mulPoly f1 f2
alg (RNeg f) = negate . f

mulPoly :: NPoly -> NPoly -> NPoly
mulPoly f1 f2 = f
    where f x = sum $ zipWith (*) coef1 coef2
            where comb = bb x
                  for1 = comb
                  for2 = map (zipWith (-) x) for1
                  coef1 = map f1 for1
                  coef2 = map f2 for2

data PairF e = Pair (Maybe (Int, e))
type Pair = Fix PairF

instance Functor PairF where
    fmap f (Pair e) = Pair $ fmap (second f) e

cartesian :: [Int] -> [Pair] -> [Pair]
cartesian xs ys = [Fix $ Pair $ Just (x, y) | x <- xs, y <- ys]

pairAlg :: PairF [Int] -> [Int]
pairAlg (Pair m) = case m of
                        Nothing -> []
                        Just (x, xs) -> x:xs

bb :: [Int] -> [[Int]]
bb xs = map (cata pairAlg) $ foldr cartesian [Fix $ Pair Nothing] $ map (\x -> [0..x]) xs
```

## Test

```haskell
module Main where

import Data.Fix
import qualified NPoly


main :: IO ()
main = do
    let added = cata NPoly.alg $ Fix (RAdd (Fix ROne) (Fix ROne))
    let multiplied = cata NPoly.alg $ Fix (RMul (Fix ROne) (Fix ROne))
    let multiplied2 = cata NPoly.alg $ Fix (RMul (Fix ROne) (Fix RZero))
    let negated = cata NPoly.alg $ Fix (RMul (Fix ROne) (Fix (RNeg (Fix ROne))))
    print $ square added
    print $ square multiplied
    print $ square multiplied2
    print $ square negated

square :: NPoly.NPoly -> [[Int]]
square poly = map f [0..3]
    where f :: Int -> [Int]
          f x = map (g x) [0..3]
            where g :: Int -> Int -> Int
                  g x y = poly [x,y]
```

## Result
```shell
ingun$ stack run
[[2,0,0],
 [0,0,0],
 [0,0,0]]

[[1,0,0],
 [0,0,0],
 [0,0,0]]

[[0,0,0],
 [0,0,0],
 [0,0,0]]

[[-1,0,0],
 [0,0,0],
 [0,0,0]]
```

First one is identity + identity 
Second one is identity * identity 
Third one is identity * zero
Fourth one is identity * -identity