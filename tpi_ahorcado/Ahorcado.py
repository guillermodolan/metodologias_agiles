class Ahorcado:
    
    # Definimos 6 vidas (cabeza, tronco, brazos (2) y piernas (2) )
    vidas = 6

    def __init__(self, palabra):
        self.palabra = palabra
    
    def ingresar_letra(self, letra):
        if letra in self.palabra:
            return True
        else:
            Ahorcado.descuenta_vida()
            return False
    
    def ingresar_palabra(self, palabra_ingresada):
        return self.palabra == palabra_ingresada
    
    @staticmethod
    def descuenta_vida():
        Ahorcado.vidas -= 1
        if Ahorcado.vidas > 0:
            return Ahorcado.vidas
        else:
            return 'Perdiste'
        
    @staticmethod
    def adivina_palabra():
        return 'Ganaste'