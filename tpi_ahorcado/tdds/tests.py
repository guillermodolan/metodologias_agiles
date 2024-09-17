import unittest
from Ahorcado import Ahorcado

class Test(unittest.TestCase):
    
    def test_ingresar_letra(self, letra):
        Ahorcado.ingresar_letra(letra)
        self.assertEqual(Ahorcado.ingresa_letra(letra), '')


if __name__ ==  '__main__':
    unittest.main()  # run all tests

