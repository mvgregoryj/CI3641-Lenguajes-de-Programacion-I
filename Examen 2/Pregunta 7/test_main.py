from unittest import TestCase
from main import *

class ManejoDeMemoriaTests(TestCase):
    
    def test_procesar(self):
        self.assertEqual(procesar("RESERVAR a aval"), "Se reservó 'a' con valor 'aval'")
        self.assertEqual(procesar("RESERVAR b bval"), "Se reservó 'b' con valor 'bval'")
        self.assertEqual(procesar("IMPRIMIR a"), 'aval')
        self.assertEqual(procesar("ASIGNAR c b"), "Se asignó 'b' a 'c'")
        self.assertEqual(procesar("IMPRIMIR c"), "bval")
        self.assertEqual(procesar("IMPRIMIR d"), "ERROR, el nombre 'd' no apunta a un valor válido")
        self.assertEqual(procesar("LIBERAR c"), "Se liberó 'c'")
        self.assertEqual(procesar("IMPRIMIR b"), "ERROR, el nombre 'b' no apunta a un valor válido")
        self.assertEqual(procesar("ASIGNAR b a"), "Se asignó 'a' a 'b'")
        self.assertEqual(procesar("IMPRIMIR b"), "aval")
        self.assertEqual(procesar("IMPRIMIR c"), "ERROR, el nombre 'c' no apunta a un valor válido")

        self.assertEqual(procesar("ASIGNAR x y"), "ERROR, el nombre 'y' no apunta a un valor válido")

        self.assertEqual(procesar("LIBERAR g"), "ERROR, el nombre 'g' no apunta a un valor válido")

        with self.assertRaises(SystemExit):
            procesar("SALIR")

        self.assertEqual(procesar("CUALQUIERCOSA"), "ERROR, ingrese una acción válida")

        self.assertEqual(procesar(""), "No ingreso ninguna accion")