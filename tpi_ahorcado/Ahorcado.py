class Ahorcado:
    
    # Definimos 6 vidas (cabeza, tronco, brazos y piernas)
    vidas = 6
    
    @staticmethod
    def ingresar_letra(letra):
        return letra
    
    @staticmethod
    def descuenta_vida():
        Ahorcado.vidas -= 1
        return Ahorcado.vidas