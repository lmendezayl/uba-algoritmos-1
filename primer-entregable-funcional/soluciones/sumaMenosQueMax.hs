-- No editar esta parte
main :: IO ()
main = do
  x <- readLn
  print (sumaMenosQueMax (x :: (Int, Int, Int)))

sumaMenosQueMax :: (Int, Int, Int) -> Bool
-- Completar acá la definición de la función

sumaMenosQueMax (t0, t1, t2) | (max3 t0 t1 t2) > ((min3 t0 t1 t2) + (medio t0 t1 t2)) = True
                             | otherwise = False

-- Pueden agregan las funciones que consideren necesarias

max3 :: Integer -> Integer -> Integer -> Integer 
max3 a b c = maximum [a, b ,c] 

min3 :: Integer -> Integer -> Integer -> Integer
min3 a b c = minimum [a, b, c]

medio3 :: Integer -> Integer -> Integer -> Integer 
medio3 a b c =  [min3 [a, b, c], _ , max3 [a, b, c]] !! 1