import string

class Ahorcado:

    def __init__(self, palabra):
        self.palabra = palabra
        self.vidas = 6 # Definimos 6 vidas (cabeza, tronco, brazos (2) y piernas (2))
        self.letras_adivinadas = []
        self.letras_erradas = []
        self.fin_de_juego = False
    
    def ingresar_letra(self, letra):
        caracteres_especiales = string.punctuation
        if not letra in caracteres_especiales or not letra.isdigit():
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
                    self.descuenta_vida()
                    print(f'Te quedan {self.vidas} vidas')
                    return False
        else:
            return False
            
            
    def arriesgar_palabra(self, palabra_ingresada):
        if not self.palabra == palabra_ingresada:
            self.descuenta_vida()
            return False
        return True
    
    
    def descuenta_vida(self):
        self.vidas -= 1
        if self.vidas > 0:
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
    
    
    def comprueba_fin_de_juego(self):
        if not '_' in self.muestra_palabra():
            self.fin_de_juego = True
        return self.fin_de_juego
    
    
    def muestra_letras_erradas(self):
        return self.letras_erradas