import unittest
from tpi_ahorcado.Ahorcado import Ahorcado

class Test(unittest.TestCase):
    
    # Done
    def test_acierta_letra(self):
        palabra = 'prueba'
        ahorcado = Ahorcado(palabra)
        letra = 'a'
        self.assertEqual(ahorcado.ingresar_letra(letra), True)

    # Done
    def test_falla_letra(self):
        palabra = 'prueba'
        ahorcado = Ahorcado(palabra)
        letra = 'g'
        self.assertEqual(ahorcado.ingresar_letra(letra), False)

    # Done
    def test_falla_letra_descuenta_vida(self):
        # Errar 1 sola vez
        Ahorcado.vidas = 6
        palabra = 'perro'
        ahorcado = Ahorcado(palabra)
        letra = 'x'
        ahorcado.ingresar_letra(letra)    
        self.assertEqual(Ahorcado.vidas, 5)

    # # In progress
    # def test_fin_de_vidas(self):
    #     # Errar 6 veces
    #     palabra = 'perro'
    #     ahorcado = Ahorcado(palabra)
    #     letra = 'x'
    #     ahorcado.ingresar_letra(letra)    
    #     self.assertEqual(Ahorcado.descuenta_vida(), False)
        
    # Done
#    def test_acierta_palabra_correcta(self):
#        palabra = 'destino'
#        ahorcado = Ahorcado(palabra)
#        palabra_ingresada = 'destino'
#        self.assertEqual(ahorcado.ingresar_palabra(palabra_ingresada), True)
#        
#    # Done
#    def test_falla_palabra_correcta(self):
#        # Un método arriesgar_palabra() que compare con la palabra en cuestión.
#        palabra = 'destino'
#        ahorcado = Ahorcado(palabra)
#        palabra_ingresada = 'ficticio'
#        self.assertEqual(ahorcado.ingresar_palabra(palabra_ingresada), False)
#        
#    # In progress
#    def test_adivina_palabra(self):
#        palabra = 'hola'
#        ahorcado = Ahorcado(palabra)
#        self.assertEqual(ahorcado.adivina_palabra(), 'Ganaste')
    
if __name__ ==  '__main__':
    unittest.main()  # run all tests