import unittest
from Ahorcado import Ahorcado

class Test(unittest.TestCase):
    
    letra = 'a'
    palabra = 'prueba'

    def test_acierta_letra(self):
        self.assertEqual(Ahorcado.ingresar_letra(Test.letra), 'a')
        
    def test_falla_letra(self):
        self.assertNotEqual(Ahorcado.ingresar_letra(Test.letra), '')
        
    def test_falla_letra_descuenta_vida(self):
        Ahorcado.vidas = 6
        self.assertEqual(Ahorcado.descuenta_vida(), 5)
        
    def test_fin_de_vidas(self):
        Ahorcado.vidas = 1
        self.assertEqual(Ahorcado.descuenta_vida(), 'Perdiste')
        
    def test_acierta_palabra(self):
        self.assertEqual(Ahorcado.ingresar_palabra(Test.palabra), 'prueba')
    
    
if __name__ ==  '__main__':
    unittest.main()  # run all tests