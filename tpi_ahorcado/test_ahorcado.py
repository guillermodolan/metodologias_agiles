import unittest
from tpi_ahorcado.Ahorcado import Ahorcado

class Test(unittest.TestCase):
    
    def test_acierta_letra(self):
        letra = 'a'
        palabra = 'prueba'
        self.assertEqual(Ahorcado.ingresar_letra(letra, palabra), True)
        
    def test_falla_letra(self):
        letra = 'g'
        palabra = 'prueba'
        self.assertEqual(Ahorcado.ingresar_letra(letra, palabra), False)
        
    def test_falla_letra_descuenta_vida(self):
        Ahorcado.vidas = 6
        self.assertEqual(Ahorcado.descuenta_vida(), 5)
        
    def test_fin_de_vidas(self):
        Ahorcado.vidas = 1
        self.assertEqual(Ahorcado.descuenta_vida(), 'Perdiste')
        
    def test_acierta_palabra_correcta(self):
        palabra_ingresada = 'destino'
        palabra_correcta = 'destino'
        self.assertEqual(Ahorcado.ingresar_palabra(palabra_ingresada, palabra_correcta), True)
        
    def test_falla_palabra_correcta(self):
        palabra_ingresada = 'destino'
        palabra_correcta = 'ficticio'
        self.assertEqual(Ahorcado.ingresar_palabra(palabra_ingresada, palabra_correcta), False)
        
    def test_adivina_palabra(self):
        self.assertEqual(Ahorcado.adivina_palabra(), 'Ganaste')
    
if __name__ ==  '__main__':
    unittest.main()  # run all tests