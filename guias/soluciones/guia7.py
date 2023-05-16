# Para definir una funcion, se usa def nombre_fun

def hola(): 
	print("Hola")

def suma2 (x: int, y: int) -> int: 
    return x + y

###################

# Guia 7: Intro a Lenguaje Imperativo

# Ejercicio 1 

# 1.1
from math import *

def raizDe2():
    return round(sqrt(2), 3)

# 1.2 
def imprimit_hola():
    print("hola")

# 1.3
def imprimir_un_verso():
    print("Vem Magalenha rojão, traz a lenha pro fogão, vem fazer armação")

# 1.4
def factorial_de_dos():
    return 2

# 1.5
def factorial_3():
    return 6

# 1.6 
def factorial_4():
    return 24

# 1.7
def factorial_5(): 
    return 120

###################

# Ejercicio 2

# 2.1
def imprimir_saludo(nombre: str) -> str:
    print("Hola " + nombre)

# 2.2 
def raiz_cuadrada_de(x: int) -> float:
    return sqrt(x)

# 2.3 
def imprimir_dos_veces(estribillo: str) -> str:
    print(estribillo * 2)

# The same string can be repeated in python by n times using string*n

# 2.4
# Opcion 1
def es_multiplo_de_v2(n: int, m: int) -> bool:
    if (n % m == 0):
        return True
    else: 
        return False

# Opcion 2
def es_multiplo_de_(n: int, m: int) -> bool:
    return (n % m == 0)

# 2.5 
def es_par(numero: int) -> bool:
    return es_multiplo_de(numero, 2)

# 2.6 (RESOLVER!!) 
# def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:    

# Ejercicio 3 

# 3.3 
def es_nombre_largo(nombre: str) -> bool:
    return (len(nombre) >= 3 and  len(nombre) <=8)

# Ejercicio 5 

# 5.1 
def devolver_el_doble_si_es_par(x: int) -> int:
    if (es_par(x)):
        return x * 2
    else: 
        return x

# 5.2 
def devolver_valor_si_es_par_sino_el_que_sigue(x: int) -> int:
    if (es_par(x)):
        return x

    else:
        return x + 1

# 5.3 
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(x: int) -> int:
    if (x % 3 == 0):
        if (x % 9 == 0):
            return x * 3
        else:
            return x * 2
    else: 
        return x

# 5.4
def nombre_muchas_letras(nombre: str) -> str:
    if (len(nombre) >= 5):
        return "Tu nombre tiene muchas letras"
    else: 
        return "Tu nombre tiene menos de 5 caracteres"

# 5.5
def vacas_o_laburo(sexo: str, edad: int) -> str:
    if (sexo == F): 
        if(edad > 18 or edad <= 60):
            return "Andá de vacaciones"
        else:
            return "Te toca trabajar"
    else: 
        if (sexo == M):
            if(edad > 18 or edad <= 60):
                return "Andá de vacaciones"
            else: 
                return "Te toca trabajar"

# 6.1
# def impr_1_al_10():


# 6.2 
def impr_10_al_40():
    i = 10
    while (i <= 40):
        print(i)
        i += 2

# 6.3 
def eco():
    i = 1
    while (i <= 10):
        print("eco")
        i +=1

# 6.4 
def despegue (num: int):
    while (num >= 1):
        print (num)
        num -= 1
    print ("Despegue")

# 6.5 
def viajeEnElTiempo (partida: int, llegada: int):
    if (partida <= llegada):
        return "No se puede viajar al pasado"
    else:
        while (partida > llegada):
            partida -= 1
            print ("Viajo al pasado, estamos en el " + str(partida))



