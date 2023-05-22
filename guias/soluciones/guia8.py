# PRIMERA PARTE

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
            break
        
def divideATodos2(s: list, e: int):
    for i in s:
        if i % e == 0:            
            return True
        else:
            return False                      
