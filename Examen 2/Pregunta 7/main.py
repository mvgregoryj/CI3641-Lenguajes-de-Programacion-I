# El programa debe tener un menú que permita al usuario elegir entre las siguientes opciones:
# 1. Reservar memoria
# 2. Asignar memoria
# 3. Liberar memoria
# 4. Imprimir valor de memoria
# 5. Salir

class Lapida():
    """
    Objeto que representa una lapida de memoria.
    """
    def __init__(self, valor = ""):
        self.valor = valor

    def __repr__(self) -> str:
        return str(self.valor)
        
class Memoria():
    """
    Memoria dinámica con liberación explícita.
    """
    def __init__(self, memoria = {}):
        self.memoria = memoria

    def reservar(self, nombre: str, valor: str) -> None:
        """
        Define un nuevo apuntador nombre que apunta a una dirección de memoria recién reservada a través de una lapida de memoria.
        """
        self.memoria[nombre] = Lapida(valor)

        return f"Se reservó '{nombre}' con valor '{self.memoria[nombre]}'"

    def asignar(self, nombre1: str, nombre2: str) -> None:
        """
        Asigna al apuntador nombre1 el apuntador nombre2. Esto crea un alias entre ambos apuntadores.
        """
        if nombre2 in self.memoria:
            self.memoria[nombre1] = self.memoria[nombre2]
            return f"Se asignó '{nombre2}' a '{nombre1}'"

        else:
            return f"ERROR, el nombre '{nombre2}' no apunta a un valor válido"

    def liberar(self, nombre: str) -> None:
        """
        Libera el espacio ocupado por el apuntador nombre.
        """
        if nombre in self.memoria:
            # del self.memoria[nombre]
            self.memoria = {key:val for key, val in self.memoria.items() if val != self.memoria[nombre]}
            return f"Se liberó '{nombre}'"
        else:
            return f"ERROR, el nombre '{nombre}' no apunta a un valor válido"

    def imprimir(self, nombre: str) -> None:
        """
        Imprime el valor de la dirección de memoria si el espacio está apuntado por nombre
        """
        if nombre in self.memoria:
            return f'{self.memoria[nombre]}'
        else:
            return f"ERROR, el nombre '{nombre}' no apunta a un valor válido"

    # def __str__(self) -> str:
    #     return f"{self.memoria}"

# Funcion que procesa la entrada del usuario y procesa la accion que desea el usuario: RESERVAR, ASIGNAR, LIBERAR memoria o SALIR del programa.
def procesar(opcion: str) -> str:

    opcion = opcion.split()

    if opcion:
        if opcion[0] == "RESERVAR" and len(opcion) == 3:
            mensaje = memoria.reservar(opcion[1], opcion[2])

        elif opcion[0] == "ASIGNAR" and len(opcion) == 3:
            mensaje = memoria.asignar(opcion[1], opcion[2])

        elif opcion[0] == "LIBERAR" and len(opcion) == 2:
            mensaje = memoria.liberar(opcion[1])

        elif opcion[0] == "IMPRIMIR" and len(opcion) == 2:
            mensaje = memoria.imprimir(opcion[1])

        elif opcion[0] == "SALIR" and len(opcion) == 1:
            exit()

        else:
            mensaje = "ERROR, ingrese una acción válida"
    
    else:
        mensaje = "No ingreso ninguna accion"

    return mensaje

# Memoria dinámica con liberación explícita.
memoria = Memoria()

if __name__ == '__main__':
    print("Manejador de memoria dinámica con liberación explícita implementado con lápidas.\n")

    print("Ingrese alguna acción valida:\nRESERVAR <nombre> <valor>\nASIGNAR <nombre1> <nombre2>\nLIBERAR <nombre>\nIMPRIMIR <nombre>\nSALIR\n")

    while True:

        opcion = input("$> ")

        resultado = procesar(opcion)
        
        print(resultado)
