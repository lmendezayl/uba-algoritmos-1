--Ejercicio 1
 
f :: Integer -> Integer
f x | x == 1 = 8
    | x == 4 = 131
    | x == 16 = 16

g :: Integer -> Integer 
g y | y == 8 = 16
    | y == 16 = 4 
    | y == 131 = 1

h = f . g
k = g . f 
 
--Ejercicio 2 
--2a
absoluto :: Integer -> Integer
absoluto x  | x < 0 = -(x)
            | otherwise = x

--2b
maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto x y | absoluto (x) > absoluto (y) = absoluto (x)
                   | otherwise = absoluto (y)

--2c
maximo3 :: Integer -> Integer -> Integer -> Integer 
maximo3 a b c | (a >= b) && (a >= c) = a
              | (a >= b) && (a <= c) = c 
              | (a <= b) && (c <= b) = b
              | otherwise = c

--2d      
{-En el siguiente caso hx2 dos interpretaciones:
"dados dos numeros racionales, decide si alguno de los dos es igual a 0"
Puede ser: 1) que devuelva un Bool
          2) que devuelva el numero que es 0-}
algunoEs0 :: Float -> Float -> Bool 
algunoEs0 x y | (x == 0) || (y == 0) = True
                 | otherwise = False

--2e
ambosSon0 :: Float -> Float -> Bool 
ambosSon0 x y | (x == 0) && (y == 0) = True
                 | otherwise = False

--2f
mismoIntervalo :: Float -> Float -> Bool 
mismoIntervalo x y | (x <= 3) && (y <= 3) = True
                   | (3 < x) && (x <= 7) && (3 < y) && (y <= 7) = True 
                   | (x > 7) && (y > 7) = True
                   | otherwise = False 

--2g
{-Esto tiene (al menos) dos interpretaciones posibles:
▶ Cuando hx2 algun numero repetido no lo sumo
    ▶ sumaDistintos(1,1,2) = 2
▶ Cuando hx2 algun numero repetido lo sumo una sola vez
    ▶ sumaDistintos(1,1,2) = 3 

Una especificacion semi-formal de la primera opcion:
problema sumaDistintos (x,y,z: Z) : Z {
    requiere: { - }
    asegura: {si los 3 parametros son distintos entonces res = x + y + z}
    asegura: {si 2 parametros son iguales, res es igual al no repetido}
    asegura: {si los 3 parametros son iguales, res = 0}
} -}

sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z | (x /= y) && (x /= z) && (y /= z) = x + y + z
                    | (x == y) && (x /= z) && (y /= z) = z
                    | (x /= y) && (x == z) && (y /= z) = y
                    | (x /= y) && (x /= z) && (y == z) = x
                    | (x == y) && (x == z) && (y == z) = 0

--2h
esMultiplo :: Integer -> Integer -> Bool
esMultiplo x y | mod x y == 0 = True
               | otherwise = False

--2i
digitoUnidades :: Int -> Int
digitoUnidades 0 = 0
digitoUnidades n = mod n 10

--2j
digitoDecenas :: Int -> Int
digitoDecenas 0 = 0
digitoDecenas n = mod (div n 10) 10

--Ejercicio 4
--4a
prodInt :: (Float, Float) -> (Float, Float) -> (Float, Float)
prodInt (x1, x2) (y1, y2) = (x1 * y1, x2 * y2)

--4b
todoMenor :: (Float, Float) -> (Float, Float) -> Bool
todoMenor (x1, x2) (y1, y2) | (x1 < y1) && (x2 < y2) = True
                            | otherwise = False

--4c
distanciaPuntos :: (Float, Float) -> (Float, Float) -> Float
distanciaPuntos (x1, x2) (y1, y2) = sqrt(((y1 - x1) ** 2) + ((x2  - y2) ** 2))

--4e 
sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer
sumarSoloMultiplos (x1, x2, x3) n | (mod x1 n == 0 ) && (mod x2 n == 0) && (mod x3 n == 0) = x1 + x2 + x3
                                  | (mod x1 n == 0 ) && (mod x2 n == 0) = x1 + x2
                                  | (mod x1 n == 0 ) && (mod x3 n == 0) = x1 + x3
                                  | (mod x2 n == 0 ) && (mod x3 n == 0) = x2 + x3
                                  | (mod x1 n == 0 ) = x1
                                  | (mod x2 n == 0 ) = x2
                                  | (mod x3 n == 0 ) = x3
                                  | otherwise = 0

--4f
posPrimerPar :: (Integer, Integer, Integer) -> Integer
posPrimerPar (x1, x2, x3) | mod x1 2 == 0 = 1
                          | mod x2 2 == 0 = 2
                          | mod x3 2 == 0 = 3 
                          | otherwise = 4

--4g 
crearPar :: a -> b -> (a, b)
crearPar a b = (a, b)

--4h
invertir ::  (a, b) ->(b, a)
invertir (a, b) = (b, a)


--Ejercicio 5 

todosMenores :: (Integer, Integer, Integer) -> Bool 
todosMenores (n1, n2, n3) | ((f5 n1) > (g5 n1)) && ((f5 n2) > (g5 n2)) && ((f5 n3) > (g5 n3)) = True
                          | otherwise = False

f5 :: Integer -> Integer
f5 n | n <= 7 = n * n
     | n > 7 = 2 * n - 1

g5 :: Integer -> Integer
g5 n = if mod n 2 == 0 then div n 2 else 3*n + 1

--Ejercicio 6 
bisiesto :: Integer -> Bool
bisiesto year | (mod year 4 /= 0) || (mod year 100 == 0 && mod year 400 /= 0) = False
              | otherwise = True

--Ejercicio 7 
distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (x1, x2, x3) (y1, y2, y3) = abs((x1 - y1) + (x2 - y2) + (x3 - y3))

--Ejercicio 8
comparar :: Integer -> Integer -> Integer
comparar a b| sumaUltimosDosDigitos a < sumaUltimosDosDigitos b = 1
                | sumaUltimosDosDigitos a > sumaUltimosDosDigitos b = -1
                | sumaUltimosDosDigitos a == sumaUltimosDosDigitos b = 0 

sumaUltimosDosDigitos :: Integer -> Integer 
sumaUltimosDosDigitos x = (mod x 10) + (mod (div x 10) 10)

