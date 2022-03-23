class Clase:
    def __init__(self, nombreClase: str, metodosPropios: list, clasePadre = None):
        self.nombreClase = nombreClase
        self.clasePadre = clasePadre

        # Metodos finales que seran los metodos iniciales mas los metodos de la clase padre
        self.metodosFinales = {}

        if isinstance(clasePadre, Clase):
            self.metodosFinales = clasePadre.metodosFinales.copy()

        # Añadimos los metodos de la claseHija, si coincide con uno de la clase padre, se reemplaza
        for m in metodosPropios:
            # Si el metodo ya existe en la clase padre, se reemplaza
            # key = nombre del metodo, value = nombre de la clase
            self.metodosFinales[m] = nombreClase


class TablasDeMetodosVirtuales:
    def __init__(self) -> None:
        # Diccionario que contiene los tipos de clases y sus métodos
        self.tabla = {}

    def definir(self, accion: list) -> str:
        claseHija = accion[0]

        # Si el nombre de la clase ya existe, no se puede definir
        if claseHija not in self.tabla:

            # Veamos que tipo de clase será, claseHija con herencia o sin herencia:

            # Si la accion[1] == ":" significa que tiene herencia de la clase con nombre accion[2] o clasePadreStr
            if accion[1] == ":":

                # Veamos si la clase padre existe
                clasePadreStr = accion[2]
                if clasePadreStr in self.tabla:
                    
                    # Si la clase padre existe, la copiamos para luego usarla para copiar los metodos a la clase hija
                    clasePadreObjeto = self.tabla[clasePadreStr]

                    # Vemos los metodos de la clase hija
                    metodosClaseHija = accion[3:]

                else:
                    return f"ERROR: la clase {clasePadreStr} no existe"

            # Si la accion[1] != ":" significa que no tiene herencia
            else:
                clasePadreObjeto = None
                metodosClaseHija = accion[1:]


            #Veamos si hay metodos repetidos:
            listTemp = [x for x in metodosClaseHija if metodosClaseHija.count(x) <= 1]

            if len(listTemp) < len(metodosClaseHija):
                return f"ERROR: todos los metodos deben llamarse diferente"

            # Creamos una nueva clase hija
            claseHijaObjeto = Clase(claseHija, metodosClaseHija, clasePadreObjeto)

            # Guardamos la clase hija en la tabla
            self.tabla[claseHija] = claseHijaObjeto

            return f"Clase {claseHija} definida con los metodos {claseHijaObjeto.metodosFinales}"

        else:
            return f"ERROR: la clase {claseHija} ya existe"
        
    def describir(self, accion: str) -> str:

        if accion[0] in self.tabla:

            clase = self.tabla[accion[0]]
            metodosClase = clase.metodosFinales.copy()

            respuesta = '\n'.join([f'{metodo} -> {metodosClase[metodo]} :: {metodo}' for metodo in metodosClase.keys()])

            return respuesta
        else:
            return f"ERROR: la clase {accion[0]} no existe"
