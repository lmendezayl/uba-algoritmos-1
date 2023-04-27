--Ejercicio 1
--1.1
longitud :: [t] -> Int
longitud xs = length xs

longitudRecursion :: [t] -> Int
longitudRecursion [] = 0
longitudRecursion (x:xs) = 1 + longitudRecursion xs 
-- (x:xs) saca la x como head xs y dsps evalia para xs, la mete 
-- de nuevo y vuelve a sacar x como head xs, y suma 1 hasta que sea []

--1.2
ultimo :: [t] -> t
ultimo xs = last xs

--1.3
principio :: [t] -> [t]
principio xs = init xs

reverso :: [t] -> [t]
reverso xs = reverse xs

--Ejercicio 2

--2.1 
pertenece :: (Eq t) => t -> [t] -> Bool 
pertenece x ys = elem x ys


