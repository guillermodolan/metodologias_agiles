# Primer actividad de práctica, realizada el 06/08/2024
# Acá hemos aplicado Unit Testing


import unittest

from Calculadora import Calculadora


class TestSuma(unittest.TestCase):

    def test_suma_uno_mas_tres(self):
        # Este caso va a ser exitoso
        Calculadora.numero1 = 1
        Calculadora.numero2 = 3
        self.assertEqual(Calculadora.sumar(), 4)

    def test_resta_ocho_menos_cinco(self):
        # Este caso va a ser erróneo
        Calculadora.numero1 = 8
        Calculadora.numero2 = 5
        # El resultado debería ser 3, pero vamos a simular que es 5
        self.assertEqual(Calculadora.restar(), 5)



if __name__ == 'main':
    unittest.main()
