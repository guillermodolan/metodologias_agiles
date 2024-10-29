import unittest
from tpi_ahorcado.Ahorcado import Ahorcado

class Test(unittest.TestCase):
    
    # Done
    def test_acierta_letra(self):
        letra = 'a'
        palabra = 'prueba'
        self.assertEqual(Ahorcado.ingresar_letra(letra, palabra), True)

    # Done
    def test_falla_letra(self):
        letra = 'g'
        palabra = 'prueba'
        self.assertEqual(Ahorcado.ingresar_letra(letra, palabra), False)

    # In progress
    def test_falla_letra_descuenta_vida(self):
        Ahorcado.vidas = 6
        letra = 'x'
        palabra = 'perro'
        Ahorcado.ingresar_letra(letra, palabra)
        self.assertEqual(Ahorcado.vidas, 5)

    # In progress
    def test_fin_de_vidas(self):
        Ahorcado.vidas = 0
        self.assertEqual(Ahorcado.descuenta_vida(), 'Perdiste')
        
    # Done
    def test_acierta_palabra_correcta(self):
        palabra_ingresada = 'destino'
        palabra_correcta = 'destino'
        self.assertEqual(Ahorcado.ingresar_palabra(palabra_ingresada, palabra_correcta), True)
    # Done
    def test_falla_palabra_correcta(self):
        palabra_ingresada = 'destino'
        palabra_correcta = 'ficticio'
        self.assertEqual(Ahorcado.ingresar_palabra(palabra_ingresada, palabra_correcta), False)
        
    # In progress
    def test_adivina_palabra(self):
        self.assertEqual(Ahorcado.adivina_palabra(), 'Ganaste')
    
if __name__ ==  '__main__':
    unittest.main()  # run all tests