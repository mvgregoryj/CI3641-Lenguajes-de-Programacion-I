"""
Implementacion de la funcion
F_{alpha,beta}(n) = n                                                                                           si 0 <= n < alpha*beta
                  = F_{alpha,beta}(n-beta*1) + F_{alpha,beta}(n-beta*2) + ... + F_{alpha,beta}(n-beta*alpha)    si n >= alpha*beta

donde:
X=3 , Y=1, Z=3

alpha = ((3 + 1) mod 5) + 3 
      = (4 mod 5) + 3
      = 4 + 3 
      = 7

beta = ((1 + 3) mod 5) + 3 
     = (4 mod 5) + 3
     = 4 + 3 
     = 7

Por lo tanto la funcion queda:

F_{7,7}(n) = n                                                          si 0 <= n < 7*7
           = F_{7,7}(n-7*1) + F_{7,7}(n-7*2) + ... + F_{7,7}(n-7*7)     si n >= 7*7

o

F_{7,7}(n) = n                                                      si 0 <= n < 49
           = F_{7,7}(n-7) + F_{7,7}(n-14) + ... + F_{7,7}(n-49)     si n >= 49

"""
import time
import matplotlib.pyplot as plt

# Version Recursiva
def alphaBetaRecursiva(n: int) -> int:

    # Casos base:
    if 0 <= n < 49:
        return n

    # No es caso base
    elif n >= 49:
        return alphaBetaRecursiva(n - 7*1) + alphaBetaRecursiva(n - 7*2) + alphaBetaRecursiva(n - 7*3) + alphaBetaRecursiva(n - 7*4) + alphaBetaRecursiva(n - 7*5) + alphaBetaRecursiva(n - 7*6) + alphaBetaRecursiva(n - 7*7)

# Version recursiva de cola
def alphaBetaRecursivaCola(n: int, sucesionAB: list, i=0) -> int:

    # Casos base:
    if 0 <= n < 49:
        return sucesionAB[n+i]

    # No es caso base
    elif n >= 49:

        # Se va ampliando la sucesionAB con elementos ya existentes bases o con los calculados e incorporados en la llamada recursiva de cola anterior. 
        # El valor de i nos servira para ir desplazandonos en la sucesionAB de la siguiente manera:
        # Por ejemplo para n = 49 el valor correspondiente será:
        # sucesionAB[49] = sucesionAB[42+0]+sucesionAB[35+0]+sucesionAB[28+0]+sucesionAB[21+0]+sucesionAB[14+0]+sucesionAB[7+0]+sucesionAB[0+0]
        # sucesionAB[50] = sucesionAB[42+1]+sucesionAB[35+1]+sucesionAB[28+1]+sucesionAB[21+1]+sucesionAB[14+1]+sucesionAB[7+1]+sucesionAB[0+1]
        # sucesionAB[51] = sucesionAB[42+2]+sucesionAB[35+2]+sucesionAB[28+2]+sucesionAB[21+2]+sucesionAB[14+2]+sucesionAB[7+2]+sucesionAB[0+2]
        # .
        # .
        # .
        # sucesionAB[100] = sucesionAB[42+51]+sucesionAB[35+51]+sucesionAB[28+51]+sucesionAB[21+51]+sucesionAB[14+51]+sucesionAB[7+51]+sucesionAB[0+51]
        sucesionAB.append(sucesionAB[42+i]+sucesionAB[35+i]+sucesionAB[28+i]+sucesionAB[21+i]+sucesionAB[14+i]+sucesionAB[7+i]+sucesionAB[0+i])
        
        return alphaBetaRecursivaCola(n - 1, sucesionAB, i+1)

# Version iterativa proveniente de la recursiva de cola
def alphaBetaIterativo(n: int) -> int:

    # lista de los primeros 49 numeros naturales
    sucesionAB = [i for i in range(49)]

    # Casos base:
    if 0 <= n < 49:
        return n

    # No es caso base
    elif n >= 49:
        # El valor de i nos servira para ir desplazandonos en la sucesionAB analogo a la recursion de cola:
        i = 0
        
        # Empezamos a agregar los valores de la sucesion correspondientes a 49 hasta n
        for k in range(49, n+1):

            # Se va ampliando la sucesionAB con elementos ya existentes bases o con los calculados e incorporados en la iteración anterior. 
            sucesionAB.append(sucesionAB[42+i]+sucesionAB[35+i]+sucesionAB[28+i]+sucesionAB[21+i]+sucesionAB[14+i]+sucesionAB[7+i]+sucesionAB[0+i])
            i += 1

        return sucesionAB[len(sucesionAB)-1]


#----------------- Comparando Recursion con Recursion de Cola e Iterativa -----------------#
if '__main__' == __name__:

    final = int(input("Ingrese el numero final de n: "))
    pasos = int(input(f"Ingrese el numero pasos desde 0 hasta {final}: "))

    # Inicializacion de variables
    valores = [i for i in range(0, final+pasos, pasos)]

    # Arreglos de tuplas con los tiempos de ejecucion de las funciones y sus respectivos resultados
    resultados_recursiva = []
    resultados_recursiva_cola = []
    resultados_iterativo = []

    for n in valores:

        # Version Recursiva
        tiempo_inicial = time.time()
        resultado = alphaBetaRecursiva(n)
        tiempo_final = time.time()

        resultados_recursiva.append((resultado, tiempo_final - tiempo_inicial))

        # Version Recursiva de cola
        # Lista de los primeros 49 numeros naturales
        listaAB = [i for i in range(49)]
    
        tiempo_inicial = time.time()
        resultado = alphaBetaRecursivaCola(n, listaAB)
        tiempo_final = time.time()

        resultados_recursiva_cola.append((resultado, tiempo_final - tiempo_inicial))

        # Version Iterativa
        tiempo_inicial = time.time()
        resultado = alphaBetaIterativo(n)
        tiempo_final = time.time()

        resultados_iterativo.append((resultado, tiempo_final - tiempo_inicial))

    # Imprimimos los resultados
    print(f"\nResultados de la ejecucion:")
    print(f"--------------------------------------------------------------------------------")
    print(f"n \t\t| Recursiva \t\t| Recursiva Cola \t| Iterativo")
    print(f"--------------------------------------------------------------------------------")
    for i in range(len(valores)):
        if resultados_recursiva[i][0] < 10000:
            print(f"{valores[i]} \t\t| {resultados_recursiva[i][0]} \t\t\t| {resultados_recursiva_cola[i][0]} \t\t\t| {resultados_iterativo[i][0]}")
        else:
            print(f"{valores[i]} \t\t| {resultados_recursiva[i][0]} \t\t| {resultados_recursiva_cola[i][0]} \t\t| {resultados_iterativo[i][0]}")

    print(f"\n\nTiempos de ejecucion en segundos:")
    print(f"--------------------------------------------------------------------------------")
    print(f"n \t\t| Recursiva \t\t| Recursiva Cola \t| Iterativo")
    print(f"--------------------------------------------------------------------------------")
    for i in range(len(valores)):
        print(f"{valores[i]} \t\t| {resultados_recursiva[i][1]:.5f} \t\t| {resultados_recursiva_cola[i][1]:.5f} \t\t| {resultados_iterativo[i][1]:.5f}")


    # Graficamos los resultados
    plt.plot(valores, [i[1] for i in resultados_recursiva], label="Recursiva")
    plt.plot(valores, [i[1] for i in resultados_recursiva_cola], label="Recursiva Cola")
    plt.plot(valores, [i[1] for i in resultados_iterativo], label="Iterativo")
    plt.xlabel("Valor de n")
    plt.ylabel("Segundos")
    plt.title("Tiempos de resultados de la ejecucion")
    plt.legend()
    plt.show()


#----------------- Comparando Recursion de Cola e Iterativa -----------------#
# if '__main__' == __name__:

#     final = int(input("Ingrese el numero final de n: "))
#     pasos = int(input(f"Ingrese el numero pasos desde 0 hasta {final}: "))

#     # Inicializacion de variables
#     valores = [i for i in range(0, final+pasos, pasos)]

#     # Arreglos de tuplas con los tiempos de ejecucion de las funciones y sus respectivos resultados
#     resultados_recursiva_cola = []
#     resultados_iterativo = []

#     for n in valores:

#         # Version Recursiva de cola
#         # Lista de los primeros 49 numeros naturales
#         listaAB = [i for i in range(49)]
        
#         tiempo_inicial = time.time()
#         resultado = alphaBetaRecursivaCola(n, listaAB)
#         tiempo_final = time.time()

#         resultados_recursiva_cola.append((resultado, tiempo_final - tiempo_inicial))

#         # Version Iterativa
#         tiempo_inicial = time.time()
#         resultado = alphaBetaIterativo(n)
#         tiempo_final = time.time()

#         resultados_iterativo.append((resultado, tiempo_final - tiempo_inicial))

#     # Imprimimos los resultados
#     print(f"\nResultados de la ejecucion:")
#     print(f"--------------------------------------------------------------------------------")
#     print(f"n \t\t| Recursiva Cola \t| Iterativo")
#     print(f"--------------------------------------------------------------------------------")
#     for i in range(len(valores)):
#         print(f"{valores[i]} \t\t| {resultados_recursiva_cola[i][0]} \t\t| {resultados_iterativo[i][0]}")

#     print(f"\n\nTiempos de ejecucion en segundos:")
#     print(f"--------------------------------------------------------------------------------")
#     print(f"n \t\t| Recursiva Cola \t| Iterativo")
#     print(f"--------------------------------------------------------------------------------")
#     for i in range(len(valores)):
#         print(f"{valores[i]} \t\t| {resultados_recursiva_cola[i][1]:.5f} \t\t| {resultados_iterativo[i][1]:.5f}")


#     # # Graficamos los resultados
#     plt.plot(valores, [i[1] for i in resultados_recursiva_cola], label="Recursiva Cola")
#     plt.plot(valores, [i[1] for i in resultados_iterativo], label="Iterativo")
#     plt.xlabel("Valor de n")
#     plt.ylabel("Segundos")
#     plt.title("Tiempos de resultados de la ejecucion")
#     plt.legend()
#     plt.show()



#----------------- Iterativa -----------------#
# if '__main__' == __name__:

#     final = int(input("Ingrese el numero final de n: "))
#     pasos = int(input(f"Ingrese el numero pasos desde 0 hasta {final}: "))

#     # Inicializacion de variables
#     valores = [i for i in range(0, final+pasos, pasos)]

#     # Arreglos de tuplas con los tiempos de ejecucion de las funciones y sus respectivos resultados
#     resultados_recursiva_cola = []
#     resultados_iterativo = []

#     for n in valores:

#         # Version Iterativa
#         tiempo_inicial = time.time()
#         resultado = alphaBetaIterativo(n)
#         tiempo_final = time.time()

#         resultados_iterativo.append((resultado, tiempo_final - tiempo_inicial))

#     # Imprimimos los resultados
#     print(f"\nResultados de la ejecucion:")
#     print(f"--------------------------------------------------------------------------------")
#     print(f"n \t\t| Iterativo")
#     print(f"--------------------------------------------------------------------------------")
#     for i in range(len(valores)):
#         print(f"{valores[i]} \t\t| {resultados_iterativo[i][0]}")

#     print(f"\n\nTiempos de ejecucion en segundos:")
#     print(f"--------------------------------------------------------------------------------")
#     print(f"n \t\t| Iterativo")
#     print(f"--------------------------------------------------------------------------------")
#     for i in range(len(valores)):
#         print(f"{valores[i]} \t\t| {resultados_iterativo[i][1]:.5f}")


#     # # Graficamos los resultados
#     plt.plot(valores, [i[1] for i in resultados_iterativo], label="Iterativo")
#     plt.xlabel("Valor de n")
#     plt.ylabel("Segundos")
#     plt.title("Tiempos de resultados de la ejecucion")
#     plt.legend()
#     plt.show()
