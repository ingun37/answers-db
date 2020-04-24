Let $`A`$ be the event of choosing the first coin, $`B`$ the second coin, $`H_i`$ the observing $`i`$ heads. They are partitions therefore

```math
P(H_3 \cup H_4 \cup H_5) = P(H_3 \cup H_4 \cup H_5|A)P(A) + P(H_3 \cup H_4 \cup H_5|B)P(B)
```

Since $`H_i`$ are all disjoint events

```math
= (P(H_3|A) + P(H_4|A) + P(H_5|A))P(A) + (P(H_3|B) + P(H_4|B) + P(H_5|B))P(B)
```

$`P(H_3|A)`$ is having three heads and two tails using the first coin.

```math
P(H_3|A) = {5 \choose 3} \left({1 \over 2}\right)^3 \left({1 \over 2}\right)^2 = {5 \choose 3}{1 \over 2^5}
```

We can calculate each terms in the same way.

```math
= ({5 \choose 3}{1 \over 2^5} 
+ {5 \choose 4}{1 \over 2^5}  
+ {5 \choose 5}{1 \over 2^5}  )P(A) + 
({5 \choose 3}{2^2 \over 3^5 }
+ {5 \choose 4}{ 2 \over 3^5}
+ {5 \choose 5}{1 \over 3^5}
)P(B)
```

Since $`P(A) = P(B) = {1 \over 2}`$

```math
= (10 + 5 + 1){1 \over 2^6} + 
(40
+ 10
+ 1
){1 \over 3^5 2} \\

\approx 0.3549
```

Here's a validating program.

```haskell
module Lib
    ( someFunc
    ) where
import System.Random
import System.Random.Shuffle
import Data.Ix
import Data.Ratio
import Data.Set hiding (map, take, filter)
import Data.List.Split

someFunc :: IO ()
someFunc = do
    problem13

problem13 :: IO ()
problem13 = do
    let seeds = [1..]
    let sampleSize = 1000000
    let samples = take sampleSize $ map pickAndFlip5 seeds
    let events = filter ((2<) . length . filter id) samples
    let eventSize = length events
    print $ approxRatio eventSize sampleSize

flipCoinN :: RandomGen g => Double -> Int -> g -> [Bool]
flipCoinN p n = map (p>) . take n . randomRs (0.0, 1.0)

pickAndFlip5 :: Int -> [Bool]
pickAndFlip5 seed = let (which, g) = (random $ mkStdGen seed)
                   in if which
                       then flipCoinN 0.5 5 g
                       else flipCoinN 0.3333333333 5 g

approxRatio :: Integral i => i -> i -> Double
approxRatio x y = fromRational $ (toInteger x) % (toInteger y)

```

Output is

```shell
0.356264
```

which is close enough to support the result.