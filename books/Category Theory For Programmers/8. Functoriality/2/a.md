```haskell
-- Equational reasoning between Maybe' and Maybe is trivial. It writes itself.
type Maybe' a = Either (Const () a) (Identity a)
maybeFrom :: Maybe' a -> Maybe a
maybeFrom (Left _) = Nothing
maybeFrom (Right (Identity a)) = Just a

maybeTo :: Maybe a -> Maybe' a
maybeTo Nothing = Left (Const ())
maybeTo (Just a) = Right (Identity a)
```