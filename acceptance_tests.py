import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class TestAhorcadoAcceptance(unittest.TestCase):

    def setUp(self):
        # Inicializa el navegador (en este caso Chrome)
        driver_path = 'C:\\metodologias_agiles\\chromedriver.exe'
        service = Service(driver_path)
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.get("http://localhost:5000")
        
    def test_configura_palabra(self):
        driver = self.driver
        # Configurar la palabra secreta
        # palabra_input = driver.find_element(By.NAME, 'palabra_input')
        palabra_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located(By.XPATH, '/html/body/div[1]/form/input'))
        palabra_input.send_keys("python")
        self.assertEqual(palabra_input.get_attribute('value'), "python")

    def test_juego_del_ahorcado(self):
        driver = self.driver
        # Verificar que la palabra está oculta y las vidas son correctas
        palabra_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located( (By.ID, 'palabra_box') ))
        # palabra_box = driver.find_element(By.ID, "palabra_box")
        self.assertNotEqual(palabra_box.text, "python")  # Debería mostrar guiones
        vidas = driver.find_element(By.ID, "vidas")
        self.assertEqual(vidas.text, "6")  # El número de vidas inicial

        # Ingresar una letra correcta
        letra_input = driver.find_element(By.ID, "letra")
        letra_input.send_keys("p")
        enviar_button = driver.find_element(By.XPATH, "//button[text()='Enviar']")
        enviar_button.click()

        # Esperar a que se actualice la interfaz
        time.sleep(2)

        # Verificar que la letra se ha acertado
        palabra_box = driver.find_element(By.ID, "palabra_box")
        self.assertIn("p", palabra_box.text)

        # Ingresar una letra incorrecta
        letra_input = driver.find_element(By.ID, "letra")
        letra_input.send_keys("z")
        enviar_button.click()

        # Esperar a que se actualice la interfaz
        time.sleep(2)

        # Verificar que las letras erradas se muestran y las vidas se actualizan
        erradas = driver.find_element(By.ID, "erradas")
        self.assertIn("z", erradas.text)
        vidas = driver.find_element(By.ID, "vidas")
        self.assertEqual(vidas.text, "5")  # Después de un error, debería haber 5 vidas restantes

        # Arriesgar una palabra incorrecta
        palabra_arriesga_input = driver.find_element(By.ID, "palabra_arriesga")
        palabra_arriesga_input.send_keys("java")
        arriesgar_button = driver.find_element(By.XPATH, "//button[text()='Enviar']")
        arriesgar_button.click()

        # Esperar a que se actualice la interfaz
        time.sleep(2)

        # Verificar si el juego terminó con la respuesta incorrecta
        alert_text = driver.switch_to.alert.text
        self.assertEqual(alert_text, "Fallaste.")  # Dependiendo de si acertó o no

        # Verificar el fin del juego
        driver.switch_to.alert.accept()  # Aceptar la alerta

    def tearDown(self):
        # Cerrar el navegador
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
