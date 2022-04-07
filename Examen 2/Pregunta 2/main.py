# Funcion evaluar recibe como argumento un operador y dos operandos y devuelve el resultado de la operacion.
def evaluar(operador: str, operandoIzq: str, operandoDer: str) -> int:
    if operador == "+":
        return int(operandoIzq) + int(operandoDer)
    elif operador == "-":
        return int(operandoIzq) - int(operandoDer)
    elif operador == "*":
        return int(operandoIzq) * int(operandoDer)
    elif operador == "/":
        return int(operandoIzq) // int(operandoDer)

# Funcion mostrar recibe como argumento un operador, dos operandos y devuelve la expresion en notacion infija.
def mostrar(operador: str, operandoIzq: str, operandoDer: str) -> str:
    if operador in "+-":
        # if len(operandoIzq) == 2 and int(operandoIzq) < 0:
        #     operandoIzq = f"({operandoIzq})"

        if len(operandoDer) == 2 and int(operandoDer) < 0:
            operandoDer = f"({operandoDer})"

        return operandoIzq + " " + operador + " " + operandoDer
    elif operador in "*/":
        if len(operandoIzq) > 1:
            operandoIzq = f"({operandoIzq})"
        if len(operandoDer) > 1:
            operandoDer = f"({operandoDer})"
        return operandoIzq + " " + operador + " " + operandoDer
        
# Funcion prefijo recibe como argumento una expresion en orden prefijo y devuelve la evaluacion de la expresion.
def prefijo(accion: str, expresion: list) -> str:
    pila = []

    # recorrer la expresion de derecha a izquierda:
    for i in range(len(expresion)-1, -1, -1):

        # si el caracter es un operador:
        if expresion[i] == "+" or expresion[i] == "-" or expresion[i] == "*" or expresion[i] == "/":
            # obtener los operandos:
            operandoIzq = pila.pop()
            operandoDer = pila.pop()

            # obtener el operador:
            operador = expresion[i]

            if accion == "EVAL":
                # calcular el resultado:
                resultado = evaluar(operador, operandoIzq, operandoDer)

            elif accion == "MOSTRAR":    
                # calcular el resultado:
                resultado = mostrar(operador, operandoIzq, operandoDer)

            # insertar el resultado en la pila:
            pila.append(f"{resultado}")

        # si el caracter es un operando:
        else:
            # insertar el operando en la pila:
            pila.append(expresion[i])

    # devolver el resultado:
    return pila[0]

# Funcion postfijo recibe como argumento una expresion en orden postfijo y devuelve la evaluacion de la expresion.
def postfijo(accion: str, expresion: list) -> str:
    pila = []

    # recorrer la expresion de izquierda a derecha:
    for i in range(0, len(expresion)):

        # si el caracter es un operador:
        if expresion[i] == "+" or expresion[i] == "-" or expresion[i] == "*" or expresion[i] == "/":
            # obtener los operandos:
            operandoDer = pila.pop()
            operandoIzq = pila.pop()

            # obtener el operador:
            operador = expresion[i]

            if accion == "EVAL":    
                # calcular el resultado:
                resultado = evaluar(operador, operandoIzq, operandoDer)

            elif accion == "MOSTRAR":    
                # calcular el resultado:
                resultado = mostrar(operador, operandoIzq, operandoDer)
                
            # insertar el resultado en la pila:
            pila.append(f"{resultado}")

        # si el caracter es un operando:
        else:
            # insertar el operando en la pila:
            pila.append(expresion[i])

    # devolver el resultado:
    return pila[0]

# Funcion que procesa la entrada del usuario y evalua una expresion, muestra una expresion o sale del programa.
def procesar(accion: str) -> str:
    
    accion = accion.strip().split()

    # Si la accion es EVAL, pedir un orden <orden> y expresion <expr> y evaluara la expresion    
    if accion[0] == "EVAL":

        # obtener el orden:
        try:
            orden = accion[1]
        except:
            return "ERROR: Faltan el argumento <orden>"

        # Si el orden no es PRE ni POST, se muestra un mensaje de ERROR.
        if orden != "PRE" and orden != "POST": 
            return "ERROR: orden no valido"

        # obtener la expresion:
        expr = accion[2:]
        if not expr:
            return "ERROR: Faltan el argumento <expr>"

        # Si el orden es PRE representa expresiones escritas en orden pre–fijo.
        if orden == "PRE":
            resultado = prefijo("EVAL", expr)
            return resultado

        # Si el orden es POST representa expresiones escritas en orden post–fijo.
        elif orden == "POST":
            resultado = postfijo("EVAL", expr)
            return resultado
        
    # Si la accion es MOSTRAR, Representa una impresión en orden in–fijo de la expresión en <expr>, que está escrita de acuerdo a <orden>.
    elif accion[0] == "MOSTRAR":

        # obtener el orden:
        try:
            orden = accion[1]
        except:
            return "ERROR: Faltan el argumento <orden>"

        # Si el orden no es PRE ni POST, se muestra un mensaje de ERROR.
        if orden != "PRE" and orden != "POST": 
            return "ERROR: orden no valido"

        # obtener la expresion:
        expr = accion[2:]
        if not expr:
            return "ERROR: Faltan el argumento <expr>"

        # Si el orden es PRE representa expresiones escritas en orden pre–fijo.
        if orden == "PRE":
            resultado = prefijo("MOSTRAR", expr)
            return resultado

        # Si el orden es POST representa expresiones escritas en orden post–fijo.
        elif orden == "POST":
            resultado = postfijo("MOSTRAR", expr)
            return resultado        

    # Si la accion es SALIR, terminar el programa.
    elif accion[0] == "SALIR":
        exit()

    else:
        return "Accion no valida"


if __name__ == "__main__":
    # Pedir al usuario repetidamente una accion: EVAL, MOSTRAR, SALIR
    while True:
        accion = input("Ingrese una accion:\nEVAL <orden> <expr>\nMOSTRAR <orden> <expr>\nSALIR\n\n")

        resultado = procesar(accion)

        print(f"{resultado}\n")