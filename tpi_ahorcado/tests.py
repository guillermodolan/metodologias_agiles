import unittest
from Ahorcado import Ahorcado

class Test(unittest.TestCase):
    
    def set_up(self):
        self.ahorcado = Ahorcado()

    def test_ingresar_letra(self):
        letra = ''
        self.assertEqual(self.ahorcado.ingresar_letra(letra), '')


if __name__ ==  '__main__':
    unittest.main()  # run all tests