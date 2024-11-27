import unittest
from Ahorcado import Ahorcado

class Test(unittest.TestCase):
    # Done
    def test_acierta_letra(self):
        palabra = 'prueba'
        ahorcado = Ahorcado(palabra)
        letra = 'a'
        self.assertEqual(ahorcado.ingresar_letra(letra), True)


    # Done
    def test_falla_letra(self):
        palabra = 'testea'
        ahorcado = Ahorcado(palabra)
        letra = 'g'
        self.assertEqual(ahorcado.ingresar_letra(letra), False)


    # Done
    def test_falla_letra_descuenta_vida(self):
        # Errar 1 sola vez
        palabra = 'conejo'
        ahorcado = Ahorcado(palabra)
        letra = 'x'
        ahorcado.ingresar_letra(letra)    
        self.assertEqual(ahorcado.vidas, 5)

    # Done
    def test_fin_de_vidas(self):
        # Errar 6 veces
        palabra = 'perro'
        ahorcado = Ahorcado(palabra)
        letras = ['x','y','z','w','t','q']
        for letra in letras:
            ahorcado.ingresar_letra(letra)
        self.assertEqual(ahorcado.vidas, 0)
        
    # Done
    def test_acierta_palabra_correcta(self):
       palabra = 'destino'
       ahorcado = Ahorcado(palabra)
       palabra_ingresada = 'destino'
       ahorcado.arriesgar_palabra(palabra_ingresada)
       self.assertEqual(ahorcado.muestra_palabra(), 'destino')
       
   # Done
    def test_falla_palabra_correcta(self):
       palabra = 'destino'
       ahorcado = Ahorcado(palabra)
       palabra_ingresada = 'ficticio'
       self.assertEqual(ahorcado.arriesgar_palabra(palabra_ingresada), False)
       
    # Done
    def test_muestra_palabra(self):
        palabra_correcta = 'Gato'
        ahorcado = Ahorcado(palabra_correcta)
        for let in palabra_correcta:
            ahorcado.ingresar_letra(let)
        self.assertEqual(ahorcado.muestra_palabra(), 'Gato')
        
    # Done
    def test_gana_juego(self):
        palabra_correcta = 'Perro'
        ahorcado = Ahorcado(palabra_correcta)
        for let in palabra_correcta:
            ahorcado.ingresar_letra(let)
        self.assertEqual(ahorcado.comprueba_fin_de_juego(), True)
    
    # Done
    def test_guarda_letras_erradas(self):
        palabra_correcta = 'pato'
        ahorcado = Ahorcado(palabra_correcta)
        letras = ['h','t','a','c','v']
        for let in letras:
            ahorcado.ingresar_letra(let)
        self.assertEqual(ahorcado.muestra_letras_erradas(),['h','c','v'])

    # Done
    def test_verifica_caracter_especial(self):
        palabra = 'scrum'
        ahorcado = Ahorcado(palabra)
        self.assertEqual(ahorcado.ingresar_letra('?'), False)
        
    # Done
    def test_verifica_numero(self):
        palabra = 'malardo'
        ahorcado = Ahorcado(palabra)
        self.assertEqual(ahorcado.ingresar_letra('5'), False)
    
    # Done
    def test_usa_comodin(self):
        palabra = 'ayuda'
        ahorcado = Ahorcado(palabra)
        self.assertEqual(ahorcado.uso_comodin() in ahorcado.palabra, True)

    # Done
    def test_usa_dos_comodines(self):
        palabra = 'help'
        ahorcado = Ahorcado(palabra)
        ahorcado.uso_comodin()
        self.assertEqual(ahorcado.uso_comodin(), None)
        
    
if __name__ ==  '__main__':
    unittest.main()  # run all tests