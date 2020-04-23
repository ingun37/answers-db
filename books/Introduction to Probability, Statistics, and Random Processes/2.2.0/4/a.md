For (a), it's multiplication of choosing 1 out of 4 aces and 4 out of the rest.

```math
\cfrac{{4 \choose 1}{48 \choose 4}}{{52 \choose 5}} \approx 0.2994736356
```

For (b)

```math
1 - \cfrac{{48 \choose 5}}{{52 \choose 5}} \approx 0.34115800166
```

## Footnotes

I was in disbelief with the result so I made a validating program to test with 999999 samples.

```haskell
module Lib
    ( someFunc, combination, hasOnly1Ace
    ) where
import System.Random
import System.Random.Shuffle
import Data.Ix
import Data.Ratio
import Data.Set hiding (map, take, filter)

someFunc :: IO ()
someFunc = do
    let sampleSize = 999999
    let seeds = range (0, sampleSize)
    let samples = map (pickRandoms 5) seeds
    let eventSize1 = length $ filter hasOnly1Ace samples
    print $ fromRational $ (toInteger eventSize1) % (toInteger sampleSize)
    let eventSize2 = length $ filter hasAtLeast1Ace samples
    print $ fromRational $ (toInteger eventSize2) % (toInteger sampleSize)

pickRandoms :: Int -> Int -> [Int]
pickRandoms n seed = take n $ randomRs (0,51) (mkStdGen seed)

seqMul :: Integer -> Integer -> Integer
seqMul x = product . range . (,) x

factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * (factorial (n-1))

combination :: Integer -> Integer -> Integer
combination n r = div (seqMul (n - r + 1) n) (factorial r)

hasOnly1Ace :: [Int] -> Bool
hasOnly1Ace arr = let a = fromList arr
                      aces = fromList [0,1,2,3]
                  in 1 == (size $ intersection a aces)

hasAtLeast1Ace :: [Int] -> Bool
hasAtLeast1Ace arr = let a = fromList arr
                         aces = fromList [0,1,2,3]
                     in 0 < (size $ intersection a aces)
```

Result was

```
0.3021743021743022
0.34475734475734476
```

which was very close to my calculation.

I learned not to believe my intuition.