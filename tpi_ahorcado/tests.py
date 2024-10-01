import unittest
from Ahorcado import Ahorcado

class Test(unittest.TestCase):
    
    letra = 'a'

    def test_acierta_letra(self):
        self.assertEqual(Ahorcado.ingresar_letra(Test.letra), 'a')
        
    def test_falla_letra(self):
        self.assertEqual(Ahorcado.ingresar_letra(Test.letra), '')


if __name__ ==  '__main__':
    unittest.main()  # run all tests