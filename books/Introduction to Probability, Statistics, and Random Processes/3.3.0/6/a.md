Let's first choose $`k`$ people from the $`N`$ guests.

```math
{N \choose k}
```

Let $`A`$ be the case that the choosen $`i`$ people get their original hats, and $`B`$ the all the other people get a wrong hat. Multiply $`A \cap B`$ to the combination and we get what we want.

```math
P(X_N = i) \\
= {N \choose k}P(A \cap B) \\
= {N \choose k}P(B|A)P(A) \\
```

$`A`$ is like permutation of all the people other than those $`k`$.

```math
= {\cfrac{N!}{k!(N - k)!}}P(B|A){\cfrac{(N-k)!}{N!}}
```

For the $`P(B|A)`$, given that those $`k`$ already got the right hats, it's simply that nobody in the rest $`N - k`$ people gets the right hat, which is $`P(X_{N-k}=0)`$.

```math
= {\cfrac{N!}{k!(N - k)!}}{P(X_{N-k}=0)}{\cfrac{(N-k)!}{N!}} \\
=  \cfrac{P(X_{N-k}=0)}{k!}
```

I've made a validation code.

```haskell
problem3_6 :: IO ()
problem3_6 = do
    let sampleSize = 999999
    let n = 5
    let k = 2
    let randomVars = take sampleSize $ map (randomVar6 n) [0..]
    let xs = filter (k==) randomVars
    print $ approxRatio (length xs) sampleSize

randomVar6 :: Int -> Int -> Int
randomVar6 n seed = length $ filter (0==) $ zipWith (-) ar sh
            where ar = [0..n-1]
                  sh = shuffle' ar n (mkStdGen seed)
```

and I tested with few different parameters and the output was clase enough to support the result.