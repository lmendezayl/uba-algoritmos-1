pascal :: Int -> [Int]
pascal 1 = [1]
pascal n = [1] ++ [x+y | (x,y) <- pares (pascal (n-1))] ++ [1]

pares :: [a] -> [(a,a)]
pares xs = zip xs (tail xs)