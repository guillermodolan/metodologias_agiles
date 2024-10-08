class Ahorcado:
    
    # Definimos 6 vidas (cabeza, tronco, brazos y piernas)
    vidas = 0
    
    @staticmethod
    def ingresar_letra(letra):
        return letra
    
    @staticmethod
    def ingresar_palabra(palabra):
        return palabra
    
    @staticmethod
    def descuenta_vida():
        Ahorcado.vidas -= 1
        if Ahorcado.vidas != 0:
            return Ahorcado.vidas
        else:
            return 'Perdiste'