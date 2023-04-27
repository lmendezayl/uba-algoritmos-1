-- No editar esta parte
main :: IO()
main = do {
  x <- readLn ;
  print(sumaPrimerosNImpares(x ::(Integer)))
  }

sumaPrimerosNImpares :: Integer -> Integer
-- Completar la definición de la función
sumaPrimerosNImpares n | n < 1 = undefined
                       | otherwise = sum [if (mod i 2 == 0) then 0 else 2*i + 2 | i <- [1..(2*n - 1)]]
-- Pueden agregan las funciones que consideren necesarias


