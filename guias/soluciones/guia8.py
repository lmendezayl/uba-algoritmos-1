# Ejercicio 1
# 1.1
# Importar modulo array
from array import *

def pertenece(s: list, e: int) -> bool:
    return (e in s)

"""def perteneceV2(s: list, e: int):
    i=0
    while (i < len(s)):
        if e == s[i]:
            return True
        else:
            i += 1"""

# 1.2 
def divideATodos(s: list([int]), e: int) -> bool:
    i = 0
    while (i <= len(s)):
        if (s[i] % e == 0):
            i += 1
        else: 
            return False
    return True
   
def divideATodos2(s: list, e: int):
    for i in s:
        if i % e == 0:            
            return True
        else:
            return False


# 1.3
def sumaTotal (lista: list) -> int:
    total = 0
    for elemento in lista:
        total += elemento
    return total

# 1.4
def ordenados(lista: list[int]) -> bool:
    elementoAnterior: int = lista[0]
    lista = lista[1::] 
    for elemento in lista:
        if elementoAnterior >= elemento:
            return False
        else:
            elementoAnterior = elemento
    return True
    
# 1.5
def palabraMayorASiete(lista: list[str]) -> bool:
    for elemento in lista:
        if len(elemento) > 7:
            return True
        else:
    return True

# 1.6
def esPalindroma(palabra: str) -> bool:
    palabra = palabra.lower()   
    for letra in palabra:  # pasa la palabra a lowercase
        if letra != palabra[-1]:  # evalua la primer letra con la ultima.
            return False
        else:
            palabra = palabra [:-1:]  # devuelve la palabra pero sin la ultima letra, s[i:j:k]
    return True