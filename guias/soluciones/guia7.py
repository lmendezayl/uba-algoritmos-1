
# Guia 7: Introduccion a Lenguaje Imperativo

from math import *

class soluciones:
    
    # Ejercicio 1. 
    # Definir las siguientes funciones y procedimientos:

    # 1.1
    def raizDe2():
        return round(sqrt(2), 3)

    # 1.2 
    def imprimir_hola():
        print("hola")

    # 1.3
    def imprimir_un_verso():
        # que imprima un verso de una cancion que vos elijas, respetando los saltos de l ́ınea.
        print("Toco y me voy, no importa cual sea el color")

    # 1.4
    def factorial_recursivo(self, n:int):
        return n * factorial(n-1)
    
    def factorial_de_dos(self):
        return self.factorial_recursivo(2)

    # 1.5
    def factorial_3(self):
        return self.factorial_recursivo(3)

    # 1.6 
    def factorial_4(self):
        return self.factorial_recursivo(4)

    # 1.7
    def factorial_5(self): 
        return self.factorial_recursivo(5)

    #########################################################

    # Ejercicio 2.
    # Definir las siguientes funciones y procedimientos con parámetros:

    # 2.1
    def imprimir_saludo(nombre: str) -> str:
        print("Hola " + nombre)

    # 2.2 
    def raiz_cuadrada_de(x: int) -> float:
        return sqrt(x)

    # 2.3 
    def imprimir_dos_veces(estribillo: str) -> str:
        print(estribillo * 2)

    # 2.4
    def es_multiplo_de_(self, n: int, m: int) -> bool:
        return (n % m == 0)

    # 2.5 
    def es_par(self, numero: int) -> bool:
        return self.es_multiplo_de(numero, 2)

    # 2.6 (RESOLVER!!) 
    def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:
        return 0    

    #########################################################

    # Ejercicio 3. 
    # Resuelva los siguientes ejercicios utilizando los operadores logicos and, or, not. 
    # Resolverlos sin utilizar alternativa condicional (if).

    # 3.1
    def alguno_es_0(numero1: float, numero2: float) -> bool:
        return (numero1 == 0 or numero2 == 0)

    # 3.2
    def ambos_es_0(numero1: float, numero2: float) -> bool:
        return (numero1 == 0 and numero2 == 0)

    # 3.3 
    def es_nombre_largo(nombre: str) -> bool:
        return (len(nombre) >= 3 and  len(nombre) <=8)

    # 3.4
    def es_bisiesto(anio: int):
        return (anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0))

    #########################################################

    # Ejercicio 4. 
    # Usando las funciones de python min y max resolver:
    # En una plantacion de pinos, de cada ́arbol se conoce la altura expresada en metros. 
    # El peso de un pino se puede estimar a partir de la altura de la siguiente manera:
    #   3 kg por cada centimetro hasta 3 metros,
    #   2 kg por cada centimetro arriba de los 3 metros. 
    # Por ejemplo: 
    #   2 metros pesan 600 kg, porque 200 * 3 = 600
    #   5 metros pesan 1300 kg, porque los primeros 3 metros pesan 900 kg y los siguientes 2 pesan los 400 restantes.
    # Los pinos se usan para llevarlos a una fabrica de muebles, a la que le sirven arboles de entre 400 y 1000 kilos, un pino fuera de este rango no le sirve a la fabrica.
    # Definir las siguientes funciones, deducir que parametros tendran a partir del enunciado. Se pueden usar funciones auxiliares si fuese necesario para aumentar la legibilidad.
    #   1. Definir la funcion peso_pino
    #   2. Definir la funcion es_peso_util, recibe un peso en kg y responde si un pino de ese peso le sirve a la fabrica.
    #   3. Definir la funcion sirve_pino, recibe la altura de un pino y responde si un pino de ese peso le sirve a la fabrica.
    #   4. Definir sirve_pino usando composicion de funciones.

    def pino_peso(self, altura: int) -> int:
        return 300 * 3 + (altura - 300) * 2 if altura > 3 else altura * 3 

    def es_peso_util(self, peso: int) -> bool:
        return (peso >= 400 and peso <= 1000)
    
    # me da paja hacer la sirve_pino sin invocar otras funciones
    def sirve_pino(self, altura: int) -> bool:
        return self.es_peso_util(self.pino_peso(altura))

    #########################################################

    # Ejercicio 5.
    # Implementar los siguientes problemas de alternativa condicional (if). 
    # Intenta especificarlos alguno de ellos (todos los que te salgan) en lenguaje semiformal y formal sin utilizar IfThenElseFi

    # 5.1 
    def devolver_el_doble_si_es_par(self, x: int) -> int:
        if (self.es_par(x)):
            return x * 2
        else: 
            return x

    # 5.2 
    def devolver_valor_si_es_par_sino_el_que_sigue(self, x: int) -> int:
        if (self.es_par(x)):
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
        if (sexo == "F"): 
            if(edad > 18 or edad <= 60):
                return "Andá de vacaciones"
            else:
                return "Te toca trabajar"
        else: 
            if (sexo == "M"):
                if(edad > 18 or edad <= 60):
                    return "Andá de vacaciones"
                else: 
                    return "Te toca trabajar"

    #########################################################

    #Ejercicio 6. Implementar las siguientes funciones usando repetici ́on condicional while:

    # 6.1
    def imprimir_1_al_10():
        i = 1
        while(i < 11):
            print(i)
            i = i + 1


    # 6.2 
    def imprimir_10_al_40():
        i = 10
        while (i <= 40):
            print(i)
            i = i + 2

    # 6.3 
    def imprimir_eco():
        i = 1
        while (i <= 10):
            print("eco")
            i = i + 1

    # 6.4
    # Escribir una funcion de cuenta regresiva para lanzar un cohete. 
    # Dicha funcion ira imprimiendo desde el numero que me pasan por parametro (que sera positivo) hasta el 1, y por ultimo “Despegue”
    def despegue (num: int):
        while (num >= 1):
            print (num)
            num -= 1
        print ("Despegue")

    # 6.5 
    # Hacer una funcion que monitoree un viaje en el tiempo. 
    # Dicha funcion recibe dos parametros, “el año de partida” y “algun año de llegada”, siendo este ultimo parametro siempre mas chico que el primero. 
    # El viaje se realizara de a saltos de un año y la funcion debe mostrar el texto: “Viajo un año al pasado, estamos en el año: <año>” cada vez que se realice un salto de año.
    def viajeEnElTiempo (partida: int, llegada: int):
        if (partida <= llegada):
            return "No se puede viajar al pasado"
        else:
            while (partida > llegada):
                partida -= 1
                print (f"Viajo al pasado, estamos en el {partida}" )

    # 6.6
    # Implementar de nuevo la funcion de monitoreo de viaje en el tiempo, pero desde el año de partida hasta lo más cercano
    # al 384 a.C., donde conoceremos a Aristóteles. Y para que sea más rápido el viaje,¡vamos a viajar de a 20 años en cada
    # salto!
    def viajeRapidoEnElTiempo(partida: int) :
        llegada = -384
        if partida <= llegada:
            return "No se puede viajar al pasado"
        else:
            while partida > llegada:
                partida -= 20
                print(f"Viajo 20 años al pasado, estamos en el año: {partida}")
            if partida < llegada:
                print("Nos pasamos un poco, pero estamos cerca de 384 a.C.")

        return f"Viaje finalizado, estamos en el año: {partida}"


    #########################################################

    # Ejercicio 7. 
    # Implementar las funciones del ejercicio 6 utilizando for num in range(i,f,p):. 
    # Recordar que la funcion range para generar una secuencia de numeros en un rango dado, con un valor inicial i, un valor final f y un paso p. 
    # Ver documentacion: https://docs.python.org/es/3/library/stdtypes.html#typesseq-range

    # 7.1
    def imprimir_1_al_10():
        for i in range(1, 11):
            print(i)


    # 7.2 
    def imprimir_10_al_40():
        for i in range(10,41):
            print(i)

    # 7.3 
    def imprimir_eco():
        for i in range(1,11):
            print("eco")

    # 7.4
    # Escribir una funcion de cuenta regresiva para lanzar un cohete. 
    # Dicha funcion ira imprimiendo desde el numero que me pasan por parametro (que sera positivo) hasta el 1, y por ultimo “Despegue”
    def despegue (num: int):
        for i in range(num, 0, -1):
            print (i)
        print ("Despegue")

    # 7.5 
    # Hacer una funcion que monitoree un viaje en el tiempo. 
    # Dicha funcion recibe dos parametros, “el año de partida” y “algun año de llegada”, siendo este ultimo parametro siempre mas chico que el primero. 
    # El viaje se realizara de a saltos de un año y la funcion debe mostrar el texto: “Viajo un año al pasado, estamos en el año: <año>” cada vez que se realice un salto de año.
    def viajeEnElTiempo(partida: int, llegada: int):
        if partida <= llegada:
            return "No se puede viajar al pasado"
        else:
            for año in range(partida, llegada, -1): 
                print(f"Viajo al pasado, estamos en el {año}")

    # 7.6
    # Implementar de nuevo la funcion de monitoreo de viaje en el tiempo, pero desde el año de partida hasta lo más cercano
    # al 384 a.C., donde conoceremos a Aristóteles. Y para que sea más rápido el viaje,¡vamos a viajar de a 20 años en cada
    # salto!
    def viajeRapidoEnElTiempo(partida: int) :
        llegada = -384
        if partida <= llegada:
            return "No se puede viajar al pasado"
        else:
            for año in range(partida, llegada, -20):
                print(f"Viajo 20 años al pasado, estamos en el año: {año}")
            if partida < llegada:
                print("Nos pasamos un poco, pero estamos cerca de 384 a.C.")
                return f"Viaje finalizado, estamos en el año: {partida}"
            
    #########################################################

    # Ejercicio 9. Sea el siguiente codigo:
    def rt(x: int, g: int) -> int:
        g = g + 1
        return x + g
    
    g: int = 0
    def ro(x: int) -> int:
        global g
        g = g + 1
        return x + g
    
    # 1. ¿Cual es el resultado de evaluar tres veces seguidas ro(1)?
    # Rta: las salidas de las tres llamadas a ro(1) son: 2, 3, 4.

    # 2. ¿Cual es el resultado de evaluar tres veces seguidas rt(1, 0)?
    # Rta: el resultado de las tres llamadas a rt(1, 0) es 2, 2, 2.

    # 4. Dar la especificacion en lenguaje natural para cada funcion, rt y ro.
    #   rt(x: int, g: int) -> int: 
    #   Esta función toma un número entero x y otro entero g. 
    #   Incrementa g en 1 y devuelve la suma de x y el nuevo valor de g. 
    #   La variable g se reinicializa en 0 en cada llamada.
    
    #   ro(x: int) -> int: 
    #   Esta función toma un número entero x. 
    #   Utiliza una variable global g, la cual se incrementa en 1 cada vez que se llama a la función. 
    #   Devuelve la suma de x y el valor actualizado de g. 
    #   La variable g se mantiene entre llamadas, por lo que cada invocación a ro afecta a las siguientes.