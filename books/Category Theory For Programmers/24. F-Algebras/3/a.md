I choosed `Rational` as type of element of Matrix because matrix is over field and rational numbers is field.
```haskell
module Lib
    ( alg, RingF(..), matalg
    ) where
import Data.Fix
import Data.Matrix

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

type Mat = Matrix Rational
matalg :: RingF Mat -> Mat
matalg RZero = zero 2 2 
matalg ROne = identity 2 
matalg (RNeg x) = fmap negate x 
matalg (RAdd x y) = elementwise (+) x y 
matalg (RMul x y) = multStd x y 
```
## Test

```haskell
main :: IO ()
main = do
    print $ cata matalg $ Fix (RAdd (Fix ROne) (Fix ROne))
```

## Result

```shell
ingun$ stack test
...
 2 % 1 0 % 1
 0 % 1 2 % 1
```