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

{- se usa el (.)para componer funciones, y se lee "f compuesta de g" 
para "f . g" -}

--Ejercicio 2 

absoluto :: Integer -> Integer
absoluto x  | x < 0 = -(x)
            | otherwise = x

maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto x y | absoluto (x) > absoluto (y) = absoluto (x)
                   | otherwise = absoluto (y)

maximo3 :: Integer -> Integer -> Integer -> Integer 
maximo3 a b c | (a >= b) && (a >= c) = a
              | (a >= b) && (a <= c) = c 
              | (a <= b) && (c <= b) = b
              | otherwise = c
            
-- En el siguiente caso hay dos interpretaciones:
-- "dados dos numeros racionales, decide si alguno de los dos es igual a 0"
-- Puede ser: 1) que devuelva un Bool
--            2) que devuelva el numero que es 0
algunoEsCero :: Float -> Float -> Bool 
algunoEsCero x y | (x == 0) || (y == 0) = True
                 | otherwise = False

ambosSonCero :: Float -> Float -> Bool 
ambosSonCero x y | (x == 0) && (y == 0) = True
                 | otherwise = False

{- dados dos numeros reales, indica si estan relacionados 
considerando la relacion de equivalencia en R
cuyas clases de equivalencia son: (−∞, 3], (3, 7] y (7, ∞), 
o dicho de otra forma, si pertenecen al mismo intervalo.-}

mismoIntervalo :: Float -> Float -> Bool 
mismoIntervalo x y | (x <= 3) && (y <= 3) = True
                   | (3 < x) && (x <= 7) && (3 < y) && (y <= 7) = True 
                   | (x > 7) && (y > 7) = True
                   | otherwise = False 

{- que dados tres numeros enteros calcule la
suma sin sumar repetidos (si los hubiera). 
Esto tiene (al menos) dos interpretaciones posibles:
▶ Cuando hay algun numero repetido no lo sumo
    ▶ sumaDistintos(1,1,2) = 2
▶ Cuando hay algun numero repetido lo sumo una sola vez
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

{- Dados dos numeros naturales, decidir si el primero es multiplo del segundo -}

esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe x y | (x mod y == 0) = True
                 | otherwise = False