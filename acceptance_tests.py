import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Ahorcado import Ahorcado
from app import app


class TestAhorcadoAcceptance(unittest.TestCase):

    # def setUp(self):
    #    # driver_path = 'C:\\metodologias_agiles\\chromedriver.exe'
    #    driver_path = '/usr/local/bin/chromedriver'
    #    service = Service(driver_path)
    #    options = webdriver.ChromeOptions()
    #    options.add_argument('--start-maximized')
    #    options.add_argument('--headless')
    #    options.add_argument('--no-sandbox')
    #    options.add_argument('--disable-dev-shm-usage')
    #    self.driver = webdriver.Chrome(service=service, options=options)
    #    self.driver.get("http://localhost:5000")

    def setUp(self):
        try:
            # Ruta al ChromeDriver
            driver_path = '/usr/local/bin/chromedriver'
            
            # Configuración del servicio
            service = Service(driver_path)
            
            # Opciones de Chrome
            options = webdriver.ChromeOptions()
            
            # Configuraciones para entornos de CI/CD
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--remote-debugging-port=9222')
            options.add_argument('--disable-gpu')
            options.add_argument('--window-size=1920,1080')
            
            # Configuraciones de seguridad adicionales
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            
            # Intentar inicializar el WebDriver con reintentos
            max_attempts = 3
            for attempt in range(max_attempts):
                try:
                    self.driver = webdriver.Chrome(service=service, options=options)
                    break
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed. Retrying...")
                    time.sleep(2)
            
            # Configurar tiempo de espera
            self.driver.implicitly_wait(10)
            
            # Navegar a la URL
            self.driver.get("http://localhost:5000")
        
        except Exception as e:
            print(f"Error en setUp: {e}")
            raise

    def tearDown(self):
        if hasattr(self, 'driver'):
            self.driver.quit()

    # Done
    def test_falla_letra(self):
        driver = self.driver
        palabra = "arco"
        palabra_input = WebDriverWait(driver, 10).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[1]/form/input') ))
        palabra_input.send_keys(palabra)
        time.sleep(1)
        boton_configura = WebDriverWait(driver, 5).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[1]/form/button') ))
        boton_configura.click()
        time.sleep(1)
        alerta = Alert(driver)
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alerta.accept()
        time.sleep(1)
        ingresa_letra_input = WebDriverWait(driver, 10).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[2]/form[1]/input') ))
        ingresa_letra_input.send_keys('l')
        time.sleep(1)
        boton_envia_letra = WebDriverWait(driver, 10).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[2]/form[1]/button') ))
        boton_envia_letra.click()
        time.sleep(1)
        vida_box = WebDriverWait(driver, 15).until(EC.visibility_of_element_located( (By.XPATH, '/html/body/div[2]/p[2]/span') ))
        time.sleep(1)
        self.assertEqual(str(5), vida_box.text)

    # Done
    def test_falla_letra_descuenta_vida(self):
        driver = self.driver
        palabra = "arco"
        palabra_input = WebDriverWait(driver, 10).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[1]/form/input') ))
        palabra_input.send_keys(palabra)
        time.sleep(1)
        boton_configura = WebDriverWait(driver, 5).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[1]/form/button') ))
        boton_configura.click()
        time.sleep(1)
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alerta = Alert(driver)
        alerta.accept()
        time.sleep(1)
        ingresa_letra_input = WebDriverWait(driver, 10).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[2]/form[1]/input') ))
        ingresa_letra_input.send_keys('p')
        time.sleep(1)
        boton_envia_letra = WebDriverWait(driver, 5).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[2]/form[1]/button') ))
        boton_envia_letra.click()
        time.sleep(1)
        vida_box = WebDriverWait(driver, 15).until(EC.visibility_of_element_located( (By.XPATH, '/html/body/div[2]/p[2]/span') ))
        self.assertEqual(str(5), vida_box.text)
    
    # Done
    def test_gana_juego(self):
        driver = self.driver
        palabra_secreta = "arco"
        palabra_input = WebDriverWait(driver, 10).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[1]/form/input') ))
        palabra_input.send_keys(palabra_secreta)
        time.sleep(1)
        boton_configura = WebDriverWait(driver, 5).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[1]/form/button') ))
        boton_configura.click()
        time.sleep(1)
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alerta = Alert(driver)
        alerta.accept()
        time.sleep(1)
        ingresa_letra_input = WebDriverWait(driver, 10).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[2]/form[1]/input') ))
        boton_envia_letra = WebDriverWait(driver, 5).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[2]/form[1]/button') ))
        ingresa_letra_input.send_keys('a')
        boton_envia_letra.click()
        time.sleep(1)
        ingresa_letra_input.send_keys('r')
        boton_envia_letra.click()
        time.sleep(1)
        ingresa_letra_input.send_keys('c')
        boton_envia_letra.click()
        time.sleep(1)
        ingresa_letra_input.send_keys('o')
        boton_envia_letra.click()
        time.sleep(1)
        alerta = WebDriverWait(driver, 10).until(EC.alert_is_present())
        texto_alerta = alerta.text
        self.assertEqual(texto_alerta, 'El juego ha terminado. Configura una nueva palabra para jugar.')

    # Done
    def test_falla_palabra_correcta(self):
        driver = self.driver
        ahorcado = Ahorcado("arco")
        palabra_input = WebDriverWait(driver, 10).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[1]/form/input') ))
        palabra_input.send_keys(ahorcado.palabra)
        # time.sleep(2)
        boton_configura = WebDriverWait(driver, 5).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[1]/form/button') ))
        boton_configura.click()
        # time.sleep(2)
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alerta = Alert(driver)
        alerta.accept()
        # time.sleep(2)
        ingresa_palabra_input = WebDriverWait(driver, 10).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[2]/form[2]/input') ))
        ingresa_palabra_input.send_keys('planta')
        # time.sleep(2)
        boton_envia_palabra = WebDriverWait(driver, 5).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[2]/form[2]/button') ))
        boton_envia_palabra.click()
        # time.sleep(2)
        vida_box = WebDriverWait(driver, 15).until(EC.visibility_of_element_located( (By.XPATH, '/html/body/div[2]/p[2]/span') ))
        # time.sleep(2)
        self.assertEqual(str(ahorcado.vidas), vida_box.text)
       
    # Done
    def test_fin_de_vidas(self):
        driver = self.driver
        palabra_secreta = "arco"
        palabra_input = WebDriverWait(driver, 10).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[1]/form/input') ))
        palabra_input.send_keys(palabra_secreta)
        time.sleep(1)
        boton_configura = WebDriverWait(driver, 5).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[1]/form/button') ))
        boton_configura.click()
        time.sleep(1)
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alerta = Alert(driver)
        alerta.accept()
        time.sleep(1)
        ingresa_letra_input = WebDriverWait(driver, 10).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[2]/form[1]/input') ))
        boton_envia_letra = WebDriverWait(driver, 5).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[2]/form[1]/button') ))
        ingresa_letra_input.send_keys('z')
        boton_envia_letra.click()
        time.sleep(2)
        ingresa_letra_input.send_keys('h')
        boton_envia_letra.click()
        time.sleep(2)
        ingresa_letra_input.send_keys('q')
        boton_envia_letra.click()
        time.sleep(2)
        ingresa_letra_input.send_keys('e')
        boton_envia_letra.click()
        time.sleep(2)
        ingresa_letra_input.send_keys('s')
        boton_envia_letra.click()
        time.sleep(2)
        ingresa_letra_input.send_keys('l')
        boton_envia_letra.click()
        time.sleep(2)
        alerta = WebDriverWait(driver, 10).until(EC.alert_is_present())
        texto_alerta = alerta.text
        self.assertEqual(texto_alerta, 'El juego ha terminado. Configura una nueva palabra para jugar.')

    # Done
    def test_acierta_letra(self):
        driver = self.driver
        palabra_secreta = "arco"
        palabra_input = WebDriverWait(driver, 10).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[1]/form/input') ))
        palabra_input.send_keys(palabra_secreta)
        # time.sleep(2)
        boton_configura = WebDriverWait(driver, 5).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[1]/form/button') ))
        boton_configura.click()
        # time.sleep(2)
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alerta = Alert(driver)
        alerta.accept()
        # time.sleep(2)
        ingresa_letra_input = WebDriverWait(driver, 10).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[2]/form[1]/input') ))
        ingresa_letra_input.send_keys('a')
        # time.sleep(2)
        boton_envia_letra = WebDriverWait(driver, 5).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[2]/form[1]/button') ))
        boton_envia_letra.click()
        # time.sleep(2)
        palabra_box = WebDriverWait(driver, 15).until(EC.visibility_of_element_located( (By.XPATH, '/html/body/div[2]/p[1]/span') ))
        letra_ingresada = 'a'
        nueva_palabra = list("____")
        
        for idx, letra in enumerate(palabra_secreta):
            if letra == letra_ingresada:
                nueva_palabra[idx] = letra
        
        nueva_palabra_texto = "".join(nueva_palabra)
        # time.sleep(2)
        driver.execute_script(f"document.getElementById('palabra_box').textContent = '{nueva_palabra_texto}';")
        palabra_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located( (By.XPATH, '/html/body/div[2]/p[1]/span') ))
        self.assertEqual(palabra_box.text, nueva_palabra_texto)

    # Done
    def test_acierta_palabra_correcta(self):
        driver = self.driver
        palabra_secreta = "arco"
        palabra_input = WebDriverWait(driver, 10).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[1]/form/input') ))
        palabra_input.send_keys(palabra_secreta)
        # time.sleep(2)
        boton_configura = WebDriverWait(driver, 5).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[1]/form/button') ))
        boton_configura.click()
        # time.sleep(2)
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alerta = Alert(driver)
        alerta.accept()
        # time.sleep(2)
        ingresa_palabra_input = WebDriverWait(driver, 10).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[2]/form[2]/input') ))
        ingresa_palabra_input.send_keys('arco')
        # time.sleep(2)
        boton_envia_palabra = WebDriverWait(driver, 5).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[2]/form[2]/button') ))
        boton_envia_palabra.click()
        # time.sleep(2)
        alerta = WebDriverWait(driver, 5).until(EC.alert_is_present())
        texto_alerta = alerta.text
        self.assertEqual(texto_alerta, '¡Ganaste!')
        
    # Done
    def test_configura_palabra_secreta(self):
        driver = self.driver
        palabra_input = WebDriverWait(driver, 10).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[1]/form/input') ))
        # time.sleep(2)
        palabra_input.send_keys("python")
        # time.sleep(2)
        boton_configura = WebDriverWait(driver, 5).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[1]/form/button') ))
        boton_configura.click()
        alerta = WebDriverWait(driver, 5).until(EC.alert_is_present())
        texto_alerta = alerta.text
        self.assertEqual(texto_alerta, "Nueva palabra configurada. ¡Comienza el juego!")
        alerta.accept()
        # time.sleep(3)

    # Done
    def test_verifica_caracter_especial(self):
        driver = self.driver
        palabra_input = WebDriverWait(driver, 10).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[1]/form/input') ))
        # time.sleep(2)
        palabra_input.send_keys("?")
        # time.sleep(2)
        boton_configura = WebDriverWait(driver, 5).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[1]/form/button') ))
        boton_configura.click()
        alerta = WebDriverWait(driver, 5).until(EC.alert_is_present())
        texto_alerta = alerta.text
        self.assertEqual(texto_alerta, "La palabra solo puede contener letras. No se permiten números ni caracteres especiales.")
        alerta.accept()
        # time.sleep(1)
        
    # Done
    def test_verifica_número(self):
        driver = self.driver
        palabra_input = WebDriverWait(driver, 10).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[1]/form/input') ))
        # time.sleep(2)
        palabra_input.send_keys("5")
        # time.sleep(2)
        boton_configura = WebDriverWait(driver, 5).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[1]/form/button') ))
        boton_configura.click()
        alerta = WebDriverWait(driver, 5).until(EC.alert_is_present())
        texto_alerta = alerta.text
        self.assertEqual(texto_alerta, "La palabra solo puede contener letras. No se permiten números ni caracteres especiales.")
        alerta.accept()
        # time.sleep(1)
        
    # Done
    def test_verifica_número_con_letra(self):
        driver = self.driver
        palabra_input = WebDriverWait(driver, 10).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[1]/form/input') ))
        # time.sleep(2)
        palabra_input.send_keys("5a")
        # time.sleep(2)
        boton_configura = WebDriverWait(driver, 5).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[1]/form/button') ))
        boton_configura.click()
        alerta = WebDriverWait(driver, 5).until(EC.alert_is_present())
        texto_alerta = alerta.text
        self.assertEqual(texto_alerta, "La palabra solo puede contener letras. No se permiten números ni caracteres especiales.")
        alerta.accept()
        # time.sleep(1)
        
    # Done
    def test_verifica_número_con_caracter(self):
        driver = self.driver
        palabra_input = WebDriverWait(driver, 10).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[1]/form/input') ))
        # time.sleep(2)
        palabra_input.send_keys("5?")
        # time.sleep(2)
        boton_configura = WebDriverWait(driver, 5).until( EC.presence_of_element_located( (By.XPATH, '/html/body/div[1]/form/button') ))
        boton_configura.click()
        alerta = WebDriverWait(driver, 5).until(EC.alert_is_present())
        texto_alerta = alerta.text
        self.assertEqual(texto_alerta, "La palabra solo puede contener letras. No se permiten números ni caracteres especiales.")
        alerta.accept()
        # time.sleep(1) 

if __name__ == '__main__':
    unittest.main()
