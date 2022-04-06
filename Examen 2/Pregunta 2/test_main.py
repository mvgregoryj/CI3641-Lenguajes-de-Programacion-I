from unittest import TestCase, expectedFailure

from main import (
    evaluar,
    mostrar,
    prefijo,
    postfijo,
    procesar,
)

class AritmeticaDeEnterosTests(TestCase):
    def test_evaluar(self):
        self.assertEqual(evaluar("+", "1", "2"), 3)
        self.assertEqual(evaluar("-", "1", "2"), -1)
        self.assertEqual(evaluar("*", "1", "2"), 2)
        self.assertEqual(evaluar("/", "1", "2"), 0)

    def test_mostrar(self):
        self.assertEqual(mostrar("+", "1", "2"), "1 + 2")
        self.assertEqual(mostrar("-", "1", "2"), "1 - 2")
        self.assertEqual(mostrar("*", "1", "2"), "1 * 2")
        self.assertEqual(mostrar("/", "1", "2"), "1 / 2")
    
    def test_prefijo(self):
        self.assertEqual(prefijo("EVAL", ["+", "1", "2"]), "3")
        self.assertEqual(prefijo("EVAL", ["-", "1", "2"]), "-1")
        self.assertEqual(prefijo("EVAL", ["*", "1", "2"]), "2")
        self.assertEqual(prefijo("EVAL", ["/", "1", "2"]), "0")  # Division entera //
        self.assertEqual(prefijo("MOSTRAR", ["+", "1", "2"]), "1 + 2")
        self.assertEqual(prefijo("MOSTRAR", ["-", "1", "2"]), "1 - 2")
        self.assertEqual(prefijo("MOSTRAR", ["*", "1", "2"]), "1 * 2")
        self.assertEqual(prefijo("MOSTRAR", ["/", "1", "2"]), "1 / 2")
    
    def test_postfijo(self):
        self.assertEqual(postfijo("EVAL", ["1", "2", "+"]), "3")
        self.assertEqual(postfijo("EVAL", ["1", "2", "-"]), "-1")
        self.assertEqual(postfijo("EVAL", ["1", "2", "*"]), "2")
        self.assertEqual(postfijo("EVAL", ["1", "2", "/"]), "0") # Division entera //
        self.assertEqual(postfijo("MOSTRAR", ["1", "2", "+"]), "1 + 2")
        self.assertEqual(postfijo("MOSTRAR", ["1", "2", "-"]), "1 - 2")
        self.assertEqual(postfijo("MOSTRAR", ["1", "2", "*"]), "1 * 2")
        self.assertEqual(postfijo("MOSTRAR", ["1", "2", "/"]), "1 / 2")

    def test_procesar(self):
        self.assertEqual(procesar("EVAL PRE + * + 3 4 5 7"), "42") 
        self.assertEqual(procesar("MOSTRAR PRE + * + 3 4 5 7"), "(3 + 4) * 5 + 7")

        self.assertEqual(procesar("EVAL PRE + * + -3 -4 -5 -7"), "28")
        self.assertEqual(procesar("MOSTRAR PRE + * + -3 -4 -5 -7"), "(-3 + (-4)) * (-5) + (-7)")

        self.assertEqual(procesar("EVAL POST 8 3 - 8 4 4 + * +"), "69")
        self.assertEqual(procesar("MOSTRAR POST 8 3 - 8 4 4 + * +"), "8 - 3 + 8 * (4 + 4)")

        self.assertEqual(procesar("EVAL POST -8 -3 - -8 -4 -4 + * +"), "59")
        self.assertEqual(procesar("MOSTRAR POST -8 -3 - -8 -4 -4 + * +"), "-8 - (-3) + (-8) * (-4 + (-4))")

        self.assertEqual(procesar("EVAL"), "ERROR: Faltan el argumento <orden>")
        self.assertEqual(procesar("EVAL PRE"), "ERROR: Faltan el argumento <expr>")
        self.assertEqual(procesar("EVAL POST"), "ERROR: Faltan el argumento <expr>")
        self.assertEqual(procesar("EVAL INF"), "ERROR: orden no valido")
        self.assertEqual(procesar("EVAL -8 -3 - -8 -4 -4 + * +"), "ERROR: orden no valido")

        self.assertEqual(procesar("MOSTRAR"), "ERROR: Faltan el argumento <orden>")
        self.assertEqual(procesar("MOSTRAR PRE"), "ERROR: Faltan el argumento <expr>")
        self.assertEqual(procesar("MOSTRAR POST"), "ERROR: Faltan el argumento <expr>")
        self.assertEqual(procesar("MOSTRAR INF"), "ERROR: orden no valido")
        self.assertEqual(procesar("MOSTRAR -8 -3 - -8 -4 -4 + * +"), "ERROR: orden no valido")

        with self.assertRaises(SystemExit):
            procesar("SALIR")

        self.assertEqual(procesar("CUALQUIERCOSA"), "Accion no valida")