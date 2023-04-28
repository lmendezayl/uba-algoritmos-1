-- DISCLAIMER: hay varios ejercicios que tienen la forma funcionP
-- Esto significa que fue creada usando funciones del Prelude de Haskell
-- y no fueron hechas usando recursion, como se pide en la guia.


--Ejercicio 1

--1.1
longitudP :: [t] -> Int
longitudP xs = length xs

longitud :: [t] -> Int
longitud [] = 0
longitud (x:xs) = 1 + longitud xs 

-- (x:xs) saca la x como head xs y dsps evalua para xs, la mete 
-- de nuevo y vuelve a sacar x como head xs, y suma 1 hasta que sea []

-- x es la head de la lista (x:xs) y xs es la tail de la lista (x:xs)

-- head xs es el primer elemento de la lista xs
-- tail xs es la lista obtenida eliminando el primer elemento de xs

--1.2
ultimoP :: [t] -> t
ultimoP xs = last xs

ultimo :: [t] -> t
ultimo (x:xs) | longitud (x:xs) == 1 = x
              | otherwise = ultimo xs

-- ultimo toma una lista (x:xs) y la evalua, si la longitud de la lista es 1
-- devuelve la head de la lista, ya que es el unico y ultimo valor; sino, devuelve la funcion
-- ultimo de la tail de la lista, hasta que cumpla el caso base. 

--1.3
principioP :: [t] -> [t]
principioP xs = init xs

principio :: [t] -> [t]
principio (x:xs) | longitud (x:xs) == 1 = []
                 | otherwise = x : principio xs

--1.4
reversoP :: [t] -> [t]
reversoP xs = reverse xs

reverso :: [t] -> [t]
reverso (x:xs) | longitud (x:xs) == 1 = (x:xs)
               | otherwise = reverso xs ++ [x]

--Ejercicio 2

--2.1 
perteneceP :: (Eq t) => t -> [t] -> Bool 
perteneceP x ys = elem x ys

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece e s | longitud s == 0 = False
              | e == head s = True
              | otherwise = pertenece e (tail s)

-- Definicion por pattern matching sacada de Wikipedia/Type_class
elemlist :: Eq a => a -> [a] -> Bool
elemlist y []     = False
elemlist y (x:xs) = (x == y) || elemlist y xs
                
--2.2
todosIguales :: (Eq t) => [t] -> Bool
todosIguales s | longitud s == 0 = True
               | head (tail s) /= head s = False
               | otherwise = todosIguales (tail s)

--2.3
todosDistintos :: (Eq t) => [t] -> Bool 
todosDistintos s | longitud s == 0 = True
                 | pertenece (head s) (tail s) == True = False
                 | otherwise = todosDistintos (tail s)

--2.4
hayRepetidos :: (Eq t) => [t] -> Bool 
hayRepetidos s | longitud s == 0 = False
               | pertenece (head s) (tail s) == True = True
               | otherwise = hayRepetidos (tail s)

--2.5
quitarP :: (Eq t) => t -> [t] -> [t] 
quitarP x xs = filter (/=x) xs

quitar :: (Eq t) => t -> [t] -> [t] 
quitar x xs | longitud xs == 0 = []
            | pertenece x xs == True = xs 