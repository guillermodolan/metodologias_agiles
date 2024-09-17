import unittest
from Ahorcado import Ahorcado

class Test(unittest.TestCase):
    
    def setUp(self):
        self.Ahorcado = Ahorcado()

    def test_ingresar_letra(self):
        letra = ''
        self.assertEqual(self.Ahorcado.ingresar_letra(letra), '')


if __name__ ==  '__main__':
    unittest.main()  # run all tests