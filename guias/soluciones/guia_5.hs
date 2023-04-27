--Ejercicio 1

--1.1
longitud :: [t] -> Int
longitud xs = length xs

longitudR :: [t] -> Int
longitudR [] = 0
longitudR (x:xs) = 1 + longitudR xs 

-- (x:xs) saca la x como head xs y dsps evalia para xs, la mete 
-- de nuevo y vuelve a sacar x como head xs, y suma 1 hasta que sea []

-- x es la head de la lista (x:xs) y xs es la tail de la lista (x:xs)
-- head xs es el primer elemento de la lista xs
-- tail xs es la lista obtenida eliminando el primer elemento de xs

--1.2
ultimo :: [t] -> t
ultimo xs = last xs

ultimoR :: [t] -> t
ultimoR (x:xs) | longitud (x:xs) == 1 = x
               | otherwise = ultimoR xs

-- ultimoR toma una lista (x:xs) y la evalua, si la longitud de la lista es 1
-- devuelve la head de la lista, ya que es el unico y ultimo valor; sino, devuelve la funcion
-- ultimoR de la tail de la lista, hasta que cumpla el caso base. 

--1.3
principio :: [t] -> [t]
principio xs = init xs

principioR :: [t] -> [t]
principioR (x:xs) | longitud (x:xs) == 1 = []
                  | otherwise = x : principioR xs

--1.4
reverso :: [t] -> [t]
reverso xs = reverse xs

reversoR :: [t] -> [t]
reversoR (x:xs) | longitud (x:xs) == 1 = (x:xs)
                | otherwise = reversoR xs ++ [x]

--Ejercicio 2

--2.1 
pertenece :: (Eq t) => t -> [t] -> Bool 
pertenece x ys = elem x ys

perteneceR :: (Eq t) => t -> [t] -> Bool
perteneceR e s | longitud s == 0 = False
               | e == head s = True
               | otherwise = perteneceR e (tail s)
                
--2.2
todosIguales :: (Eq t) => [t] -> Bool
todosIguales s | longitud s == 0 = True
               | head (tail s) /= head s = False
               | otherwise = todosIguales (tail s)

--2.3
todosDistintos :: (Eq t) => [t] -> Bool 
todosDistintos s | longitud s == 0 = True
                 | perteneceR (head s) (tail s) == True = False
                 | otherwise = todosDistintos (tail s)
