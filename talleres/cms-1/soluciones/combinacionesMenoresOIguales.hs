-- No editar esta parte
main :: IO()
main = do {
  x <- readLn ;
  print(combinacionesMenoresOiguales(x ::(Integer)))
  }

combinacionesMenoresOiguales :: Integer -> Integer
-- Completar la definición de la función
combinacionesMenoresOiguales n | n < 1 = undefined
                               | otherwise = sum [if i*j <= n then 1 else 0 | i <- [1..n], j <- [1..n]]
-- Pueden agregan las funciones que consideren necesarias



