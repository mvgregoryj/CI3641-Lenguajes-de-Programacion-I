from unittest import TestCase

from main import *

class CreadorDeClasesTests(TestCase):
    def test_procesar(self):
        self.assertEqual(procesar("CLASS A f g"), "Clase A definida con los metodos {'f': 'A', 'g': 'A'}")
        self.assertEqual(procesar("CLASS B : A f h"), "Clase B definida con los metodos {'f': 'B', 'g': 'A', 'h': 'B'}")
        self.assertEqual(procesar("DESCRIBIR A"), "f -> A :: f\ng -> A :: g")
        self.assertEqual(procesar("DESCRIBIR B"), "f -> B :: f\ng -> A :: g\nh -> B :: h")
        self.assertEqual(procesar("CLASS C : D f h"), "ERROR: la clase D no existe")
        self.assertEqual(procesar("CUALQUIERCOSA"), "ERROR, ingrese una acción válida")
        self.assertEqual(procesar(""), "No ingreso ninguna accion")
        self.assertEqual(procesar("CLASS E f g a a b"), "ERROR: todos los metodos deben llamarse diferente")
        self.assertEqual(procesar("CLASS A f g"), "ERROR: la clase A ya existe")
        self.assertEqual(procesar("DESCRIBIR G"), "ERROR: la clase G no existe")

         

        with self.assertRaises(SystemExit):
            procesar("SALIR")
