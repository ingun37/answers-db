```haskell
module Un
    ( primes
    ) where

import Data.List

primes :: [Int]
primes = unfoldr (\(prime:remains) -> Just (prime, filter (notdiv prime) remains)) [2..]
    where notdiv p n = n `mod` p /= 0
```