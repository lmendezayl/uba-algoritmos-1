-- Ejercicio 1
fibonacci :: Integer -> Integer
fibonacci n | n == 0 = 0
            | n == 1 = 1
            | n >= 1 = (fibonacci (n-1) + fibonacci (n-1))
            | otherwise = undefined

--Ejercico 2 
parteEntera :: Float -> Integer
parteEntera n | 0 <= n && n < 1 = 0
              | n > -1  && n < 0 = -1
              | n >=1 = 1 + parteEntera (n-1)
              | otherwise = (-1) + parteEntera (n+1)

-- Ejercico 3 
esDivisible :: Integer -> Integer -> Bool
esDivisible n x | n == 0 = True
                | n < x = False
                | x < 0 = esDivisible (n+x) x
                | otherwise = esDivisible (n-x) x
-- Ejercicio 4 
sumaImpares :: Integer -> Integer
sumaImpares n | n == 0 = 0
              | otherwise = (sumaImpares (n-1)) + (2*n-1)
-- Ejercicio 5 
medioFact :: Integer ->Integer
medioFact n | n == 0  || n == (-1) = 1
            | otherwise = n * (medioFact (n-2))

--Ejercicio 6
sumaDigitos :: Integer ->Integer
sumaDigitos 0 = 0
sumaDigitos n = mod n 10 + sumaDigitos (div n 10)

--mod n 10 → me da el ultimo digito de n.
--div n 10 → le saca el ultimo digito a n

-- Ejercicio 7
todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | n == mod n 10 = True
                      | mod (div n 10) 10 /= mod n 10 = False
                      | otherwise = todosDigitosIguales (div n 10)

-- Ejercico 8 
iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i | i == cantDigitos n = mod n 10
                 | otherwise = iesimoDigito (div n 10 ) i

cantDigitos :: Integer -> Integer
cantDigitos n | n < 10 = 1
              | otherwise = 1 + cantDigitos (div n 10)

--Ejercicio 9 
esCapicua :: Integer -> Bool
esCapicua n = (show n) == reverse (show n)

--Ejercicio 10
--10a 
f1 :: Integer -> Integer 
f1 0 = 1
f1 n = (-1) + 2^(n + 1)

--10b
f2 :: Integer -> Float -> Float
f2 n q | n == 1 = q
       | otherwise = q^n  + f2 (n - 1) q

--10c
f3 :: Integer -> Float -> Float
f3 n q | n == 1 = q^2 + q 
       | otherwise = q^(2*n) + q^(2*n - 1) + f3 (n - 1) q

--10d
f4 :: Integer -> Float -> Float 
f4 n q = f3 n q - f2 (n-1) q