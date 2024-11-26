from selenium import webdriver
from selenium.webdriver.ie.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import unittest

class AcceptanceTests(unittest.TestCase):
    def setUp(self):
        self.driver_path = 'D:\\metodologias_agiles\\chromedriver.exe'  # Asegúrate de que esta ruta sea correcta
        self.service = Service(self.driver_path)
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.driver.get("http://127.0.0.1:5000/")

    def test_ingresar_letra_correcta(self):
        driver = self.driver
        letra_input = driver.find_element(By.ID, "letra")  # Campo de entrada para la letra
        letra_input.send_keys("p")
        letra_input.send_keys(Keys.RETURN)
        
        # Espera hasta que el elemento con ID "palabra" contenga la letra "p"
        WebDriverWait(driver, 3).until(
            EC.text_to_be_present_in_element((By.ID, "palabra"), "p")
        )
        palabra = driver.find_element(By.ID, "palabra").text
        self.assertIn("p", palabra)

    def test_arriesgar_palabra_correcta(self):
        driver = self.driver
        # Cambiar este ID si el campo de entrada de la palabra es distinto
        palabra_input = driver.find_element(By.ID, "letra")
        palabra_input.send_keys("python")
        palabra_input.send_keys(Keys.RETURN)

        # Espera explícita hasta que la alerta esté presente
        WebDriverWait(driver, 3).until(EC.alert_is_present())

        alert = driver.switch_to.alert
        self.assertEqual(alert.text, "¡Ganaste!")
        alert.accept()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
