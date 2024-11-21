from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

class TestAhorcadoFrontend(unittest.TestCase):
    def setUp(self):
        # Configurar el driver (asegúrate de que ChromeDriver esté instalado y en el PATH)
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:5000")  # Cambia al puerto donde esté corriendo Flask

    def test_juego_completo(self):
        driver = self.driver
        
        # Verificar título de la página
        self.assertEqual(driver.title, "Juego del Ahorcado")

        # Iniciar el juego con la palabra secreta
        palabra_input = driver.find_element(By.ID, "palabra")
        palabra_input.send_keys("python")
        iniciar_button = driver.find_element(By.XPATH, "//button[text()='Iniciar Juego']")
        iniciar_button.click()

        # Esperar a que se cargue el juego
        time.sleep(1)

        # Verificar que el estado inicial sea correcto
        estado_text = driver.find_element(By.ID, "estado").text
        self.assertTrue("Palabra: ______" in estado_text)

        # Adivinar una letra correcta
        letra_input = driver.find_element(By.ID, "letra")
        letra_input.send_keys("p")
        adivinar_button = driver.find_element(By.XPATH, "//button[text()='Adivinar']")
        adivinar_button.click()
        
        time.sleep(1)  # Esperar respuesta del servidor

        # Verificar que la letra acertada se muestre
        estado_text = driver.find_element(By.ID, "estado").text
        self.assertTrue("Palabra: p_____" in estado_text)

        # Adivinar una letra incorrecta
        letra_input.clear()
        letra_input.send_keys("z")
        adivinar_button.click()

        time.sleep(1)

        # Verificar que las vidas disminuyen
        vidas_text = driver.find_element(By.ID, "vidas").text
        self.assertTrue("Vidas restantes: 5" in vidas_text)

        # Usar comodín
        comodin_button = driver.find_element(By.XPATH, "//button[text()='Usar Comodín']")
        comodin_button.click()

        time.sleep(1)

        # Verificar que el comodín se utilizó
        mensaje_text = driver.find_element(By.ID, "mensaje").text
        self.assertIn("¡Comodín usado con éxito!", mensaje_text)

        # Terminar el juego adivinando todas las letras restantes
        for letra in "ython":
            letra_input.clear()
            letra_input.send_keys(letra)
            adivinar_button.click()
            time.sleep(0.5)

        # Verificar mensaje de fin del juego
        alert = driver.switch_to.alert
        self.assertIn("¡El juego ha terminado!", alert.text)
        alert.accept()

    def tearDown(self):
        # Cerrar el navegador
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
