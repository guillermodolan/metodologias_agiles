class Ahorcado:
    
    # Definimos 6 vidas (cabeza, tronco, brazos y piernas)
    vida_maxima = 6
    
    @staticmethod
    def ingresar_letra(letra, palabra):
        if letra in palabra:
            return True
        else:
            return False
    
    @staticmethod
    def ingresar_palabra(palabra_ingresada, palabra_correcta):
        return palabra_correcta == palabra_ingresada
    
    @staticmethod
    def descuenta_vida():
        Ahorcado.vidas -= 1
        if Ahorcado.vidas != 0:
            return Ahorcado.vidas
        else:
            return 'Perdiste'
        
    @staticmethod
    def adivina_palabra():
        return 'Ganaste'