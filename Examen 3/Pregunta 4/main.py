# Define un nuevo tipo que poseerá métodos con nombres establecidos en la lista proporcionada. El <tipo> puede ser:
# • Un nombre, que establece un tipo que no hereda de ningún otro.
# • Una expresión de la forma <nombre> : <super>, que establece el nombre del tipo y el hecho de que este tipo hereda del tipo con nombre <super>.
# Por ejemplo: CLASS A f g y CLASS B : A f h
#
# Notemos que es posible reemplazar definiciones de una super clase en clases que la heredan.
#
# El programa debe reportar un error e ignorar la acción si el nombre de la nueva clase ya existe, si la clase super no existe, si hay definiciones repetidas en la lista de nombres de métodos o si se genera un ciclo en la jerarquía de herencia.


from objetos import *

tmv = TablasDeMetodosVirtuales()

# Funcion que procesa la entrada del usuario y Define un nuevo tipo, muestra la tabla de métodos virtuales o sale del programa.
def procesar(accion: str) -> str:
    
    accion = accion.strip().split()

    if accion:
        if accion[0] == "CLASS":
            mensaje = tmv.definir(accion[1:])
        elif accion[0] == "DESCRIBIR":
            mensaje = tmv.describir(accion[1:])
        elif accion[0] == "SALIR":
            exit()

        else:
            mensaje = "ERROR, ingrese una acción válida"
    else:
        mensaje = "No ingreso ninguna accion"
    
    return mensaje

if __name__ == "__main__":
    # Pedir al usuario repetidamente una accion: CLASS, DESCRIBIR, SALIR

    while True:
        print("\nIngrese una accion:\nCLASS <tipo> [<nombre>]\nDESCRIBIR <nombre> <expr>\nSALIR\n\n")

        accion = input("$> ")

        resultado = procesar(accion)

        if not resultado.startswith("Clase"):
            print(f"{resultado}")
