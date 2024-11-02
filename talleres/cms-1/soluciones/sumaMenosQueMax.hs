-- No editar esta parte
main :: IO ()
main = do
  x <- readLn
  print (sumaMenosQueMax (x :: (Int, Int, Int)))

sumaMenosQueMax :: (Int, Int, Int) -> Bool
-- Completar acá la definición de la función

sumaMenosQueMax (t0, t1, t2) | (max3 t0 t1 t2) > ((min3 t0 t1 t2) + (medio3 t0 t1 t2)) = True
                             | otherwise = False

-- Pueden agregan las funciones que consideren necesarias

medio3 :: Int -> Int -> Int -> Int 
medio3 a b c =  [minimum [a, b, c], (a + b + c - (minimum [a, b, c]) - (maximum [a, b, c])), maximum [a, b, c]] !! 1

max3 :: Int -> Int -> Int -> Int 
max3 a b c = maximum [a, b ,c] 

min3 :: Int -> Int -> Int -> Int
min3 a b c = minimum [a, b, c]
