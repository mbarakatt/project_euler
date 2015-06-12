import Data.MemoCombinators


p=[200,100,50,20,10,5,2,1]

f2 ([]) _ _ = []
f2 (h:t) a b = f (a-h) (minimum [h,a-h]) :f2 t a b

f ::  Int -> Int -> Integer
f = memo2 integral integral f'
  where
    f' a 1 = 1
    f' a b = (if  a==b && a `elem` p then 1 else 0 ) + sum (f2 [c | c <- p, c<=b] a b )

prob31 a = f a a

main = putStrLn $ show $ prob31 200
