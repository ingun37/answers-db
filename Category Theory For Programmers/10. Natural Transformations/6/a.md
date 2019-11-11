```haskell
import Data.Functor.Contravariant

op :: Op Bool Int
op = Op (\x -> x > 0)


tc1 :: Op Bool a -> Op Float a
tc1 (Op f) = Op (\x -> if f x then 1 else 0)

test :: (Op Float String) -> Float
test (Op f) = f "5"

tc1out1 :: IO ()
tc1out1 = do
    let o1 = (contramap read . tc1) op
    let o2 = (tc1 . contramap read) op
    print (test o1 == test o2)
```