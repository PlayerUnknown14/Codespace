import Data.Array
import Data.List (tails, inits)

ps = 2 : [n | (r:q:_, px) <- (zip . tails . (2:) . map (^2)) ps (inits ps),
              (n,True)    <- assocs (
                                accumArray (\_ _ -> False) True (r+1,q-1)
                     [(m,()) | p <- px, 
                               let s = div (r+p) p * p,  m <- [s,s+p..q-1]] )]