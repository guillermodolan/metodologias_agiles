import unittest
from app import app
from Ahorcado import Ahorcado

class Test(unittest.TestCase):
    """Clase implementada como módulo de tests de Back-End."""

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        """Test que verifica la ruta principal"""
        self.app.post('/configurar_palabra', data={'palabra': 'indice'})
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_configurar_palabra(self):
        """Test que verifica que se configure una palabra"""
        response = self.app.post('/configurar_palabra', data={'palabra': 'python'})
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertEqual(json_data['palabra'], '______')
        self.assertEqual(json_data['vidas'], 6)
        self.assertEqual(json_data['erradas'], [])

    def test_acierta_letra(self):
        """Test que verifica que se acierte una letra"""
        palabra = 'prueba'
        ahorcado = Ahorcado(palabra)
        letra = 'a'
        self.assertTrue(ahorcado.ingresar_letra(letra))

    def test_acierta_letra_app(self):
        """Test que verifica que se acierte una letra desde la 
        aplicación"""
        self.app.post('/configurar_palabra', data={'palabra': 'prueba'})
        response = self.app.post('/ingresar_letra', data={'letra': 'a'})
        json_data = response.get_json()
        self.assertTrue(json_data['acierto'])
        self.assertEqual(json_data['palabra'], '_____a')
        self.assertEqual(json_data['vidas'], 6)

    def test_falla_letra(self):
        """Test que verifica que falla una letra"""
        palabra = 'testea'
        ahorcado = Ahorcado(palabra)
        letra = 'g'
        self.assertFalse(ahorcado.ingresar_letra(letra))

    def test_falla_letra_app(self):
        """Test que verifica que se descuente una vida al falla una letra
        desde la aplicación"""
        self.app.post('/configurar_palabra', data={'palabra': 'testea'})
        response = self.app.post('/ingresar_letra', data={'letra': 'g'})
        json_data = response.get_json()
        self.assertFalse(json_data['acierto'])
        self.assertEqual(json_data['vidas'], 5)
        self.assertIn('g', json_data['erradas'])

    def test_falla_letra_descuenta_vida(self):
        """Test que verifica que se descuente una vida al falla una letra"""
        palabra = 'conejo'
        ahorcado = Ahorcado(palabra)
        letra = 'x'
        ahorcado.ingresar_letra(letra)
        self.assertEqual(ahorcado.vidas, 5)

    def test_fin_de_vidas(self):
        """Test que verifica el fin de vidas"""
        palabra = 'perro'
        ahorcado = Ahorcado(palabra)
        letras = ['x','y','z','w','t','q']
        for letra in letras:
            ahorcado.ingresar_letra(letra)
        self.assertEqual(ahorcado.vidas, 0)

    def test_fin_de_vidas_app(self):
        """Test que verifica el fin de vidas desde la aplicación"""
        self.app.post('/configurar_palabra', data={'palabra': 'perro'})
        for letra in ['x', 'y', 'z', 'w', 't']:
            self.app.post('/ingresar_letra', data={'letra': letra})
        response = self.app.post('/ingresar_letra', data={'letra': 'q'})
        json_data = response.get_json()
        self.assertTrue(json_data['fin_juego'])
        self.assertTrue(json_data['reiniciar'])

    def test_acierta_palabra_correcta(self):
        """Test que verifica que se acierte la palabra correcta"""
        palabra = 'destino'
        ahorcado = Ahorcado(palabra)
        palabra_ingresada = 'destino'
        ahorcado.arriesgar_palabra(palabra_ingresada)
        self.assertEqual(ahorcado.muestra_palabra(), 'destino')

    def test_acierta_palabra_correcta_app(self):
        """Test que verifica que se acierte la palabra correcta desde la aplicación"""
        self.app.post('/configurar_palabra', data={'palabra': 'destino'})
        response = self.app.post('/arriesgar_palabra', data={'palabra_arriesga': 'destino'})
        json_data = response.get_json()
        self.assertTrue(json_data['resultado'])

    def test_falla_palabra_correcta(self):
        """Test que verifica que falle la palabra correcta"""
        palabra = 'destino'
        ahorcado = Ahorcado(palabra)
        palabra_ingresada = 'ficticio'
        self.assertFalse(ahorcado.arriesgar_palabra(palabra_ingresada))
        self.assertEqual(ahorcado.vidas, 5)

    def test_arriesgar_palabra_incorrecta(self):
        """Test que verifica que se arriesgue una palabra incorrecta"""
        self.app.post('/configurar_palabra', data={'palabra': 'python'})
        response = self.app.post('/arriesgar_palabra', data={'palabra_arriesga': 'java'})
        json_data = response.get_json()
        self.assertFalse(json_data['resultado'])
        self.assertEqual(json_data['vidas'], 5)

    def test_muestra_palabra(self):
        """Test que verifica que se muestre la palabra"""
        palabra_correcta = 'Gato'
        ahorcado = Ahorcado(palabra_correcta)
        for let in palabra_correcta:
            ahorcado.ingresar_letra(let)
        self.assertEqual(ahorcado.muestra_palabra(), 'Gato')

    def test_gana_juego(self):
        """Test que verifica que se gane un juego"""
        palabra_correcta = 'Perro'
        ahorcado = Ahorcado(palabra_correcta)
        for let in palabra_correcta:
            ahorcado.ingresar_letra(let)
        self.assertTrue(ahorcado.comprueba_fin_de_juego())

    def test_guarda_letras_erradas(self):
        """Test que verifica que se guarden letras erradas"""
        palabra_correcta = 'pato'
        ahorcado = Ahorcado(palabra_correcta)
        letras = ['h','t','a','c','v']
        for let in letras:
            ahorcado.ingresar_letra(let)
        self.assertEqual(ahorcado.muestra_letras_erradas(),['h','c','v'])

    def test_verifica_caracter_especial(self):
        """Test que verifica que no se ingresen caracteres especiales"""
        palabra = 'scrum'
        ahorcado = Ahorcado(palabra)
        self.assertFalse(ahorcado.ingresar_letra('?'))

    def test_verifica_numero(self):
        """Test que verifica que no se ingresen números"""
        palabra = 'accesible'
        ahorcado = Ahorcado(palabra)
        self.assertFalse(ahorcado.ingresar_letra('5'))

    def test_usar_comodin(self):
        """Test que verifica que el comodin funcione bien"""
        palabra = 'ayuda'
        ahorcado = Ahorcado(palabra)
        self.assertIn(ahorcado.uso_comodin(), ahorcado.palabra)

    def test_usar_comodin_app(self):
        """Test que verifica que el comodin funcione bien en el flujo de aplicación"""
        self.app.post('/configurar_palabra', data={'palabra': 'ayuda'})
        response = self.app.post('/usar_comodin')
        json_data = response.get_json()
        self.assertIn(json_data['letra_comodin'], 'ayuda')

    def test_usar_dos_comodines(self):
        """Test que verifica que no se utilicen 2 comodines"""
        palabra = 'help'
        ahorcado = Ahorcado(palabra)
        ahorcado.uso_comodin()
        self.assertEqual(ahorcado.uso_comodin(), None)

    def test_reiniciar(self):
        """Test que verifica el reinicio del juego"""
        self.app.post('/configurar_palabra', data={'palabra': 'python'})
        response = self.app.post('/reiniciar')
        json_data = response.get_json()
        self.assertEqual(json_data['message'], "Juego reiniciado.")


if __name__ ==  '__main__':
    unittest.main()  # run all tests
