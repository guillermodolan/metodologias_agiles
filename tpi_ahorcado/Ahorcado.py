class Ahorcado:
    
    # Definimos 6 vidas (cabeza, tronco, brazos (2) y piernas (2))
    vidas = 6

    def __init__(self, palabra):
        self.palabra = palabra
        self.letras_adivinadas = []
        self.letras_erradas = []
    
    def ingresar_letra(self, letra):
        if letra in self.letras_adivinadas or letra in self.letras_erradas:
            print('Ya has ingresado esa letra. Por favor ingresá otra.')
        else:
            if letra in self.palabra:
                self.letras_adivinadas.append(letra)
                self.muestra_palabra()
                print('Acertaste. ¡Continúa así!')
                return True
            else:
                self.letras_erradas.append(letra)
                print(f'Letras erradas: {self.letras_erradas}')
                print(f'Perdiste una vida.')
                Ahorcado.descuenta_vida()
                print(f'Te quedan {Ahorcado.vidas} vidas')
                return False
            
    
    def arriesgar_palabra(self, palabra_ingresada):
        if not self.palabra == palabra_ingresada:
            Ahorcado.descuenta_vida()
            return False
        return True
    
    @staticmethod
    def descuenta_vida():
        Ahorcado.vidas -= 1
        if Ahorcado.vidas > 0:
            return True
        else:
            return False
        
    @staticmethod
    def adivina_palabra():
        return 'Ganaste'

    def muestra_palabra(self):
        palabra_actual = ''
        for letra in self.palabra:
            if letra in self.letras_adivinadas:
                palabra_actual = palabra_actual + letra
            else:
                palabra_actual = palabra_actual + '_'
        return palabra_actual