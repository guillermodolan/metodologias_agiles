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


    # Done
    def test_fin_de_vidas(self):
        # Errar 6 veces
        Ahorcado.vidas = 6
        palabra = 'perro'
        ahorcado = Ahorcado(palabra)
        letras = ['x','y','z','w','t','q']
        for letra in letras:
            ahorcado.ingresar_letra(letra)
        self.assertEqual(Ahorcado.vidas, 0)
        
    # Done
    def test_acierta_palabra_correcta(self):
       palabra = 'destino'
       ahorcado = Ahorcado(palabra)
       palabra_ingresada = 'destino'
       self.assertEqual(ahorcado.arriesgar_palabra(palabra_ingresada), True)
       
       
   # Done
    def test_falla_palabra_correcta(self):
       palabra = 'destino'
       ahorcado = Ahorcado(palabra)
       palabra_ingresada = 'ficticio'
       self.assertEqual(ahorcado.arriesgar_palabra(palabra_ingresada), False)
       
       
    # Done
    def test_muestra_palabra(self):
        palabra_correcta = 'Perro'
        ahorcado = Ahorcado(palabra_correcta)
        for let in palabra_correcta:
            ahorcado.ingresar_letra(let)
        self.assertEqual(ahorcado.muestra_palabra(), 'Perro')
        
    # Done
    def test_gana_juego(self):
        palabra_correcta = 'Perro'
        ahorcado = Ahorcado(palabra_correcta)
        for let in palabra_correcta:
            ahorcado.ingresar_letra(let)
        self.assertEqual(ahorcado.comprueba_fin_de_juego(), True)
        
    
    # Done
    def test_guarda_letras_erradas(self):
        palabra_correcta = 'Pato'
        ahorcado = Ahorcado(palabra_correcta)
        letras = ['h','t','a','c','v']
        for let in letras:
            ahorcado.ingresar_letra(let)
        self.assertEqual(ahorcado.muestra_letras_erradas(),['h','c','v'])
    
if __name__ ==  '__main__':
    unittest.main()  # run all tests