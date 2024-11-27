import string, random

class Ahorcado:

    def __init__(self, palabra):
        self.palabra = palabra
        self.vidas = 6 # Definimos 6 vidas (cabeza, tronco, brazos (2) y piernas (2))
        self.letras_adivinadas = []
        self.letras_erradas = []
        self.comodin = 1
        self.fin_de_juego = False
        
        
    def comprueba_letra_repetida(self, letra):
        if letra in self.letras_adivinadas or letra in self.letras_erradas:
            return True
        else:
            return False
    
    
    def ingresar_letra(self, letra):
        caracteres_especiales = string.punctuation
        if not letra in caracteres_especiales or not letra.isdigit():
            if self.comprueba_letra_repetida(letra):
                print('Ya has ingresado esa letra. Por favor ingresá otra.')
                return False
            else:
                if letra.lower() in self.palabra.lower():
                    print(letra.lower())
                    print(self.palabra.lower())
                    self.letras_adivinadas.append(letra.lower())
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
        if self.palabra.lower() != palabra_ingresada.lower(): # Acá ignoro mayúsculas y minúsculas
            self.descuenta_vida()
            return False
        else:
            self.letras_adivinadas = list(self.palabra)
            self.fin_de_juego = True
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
            if letra.lower() in self.letras_adivinadas:
                palabra_actual = palabra_actual + letra
            else:
                palabra_actual = palabra_actual + '_'
        return palabra_actual
    
    
    def comprueba_fin_de_juego(self):
        if not '_' in self.muestra_palabra() or self.vidas == 0:
            self.fin_de_juego = True
        return self.fin_de_juego
    
    
    def muestra_letras_erradas(self):
        return self.letras_erradas
    
    
    def uso_comodin(self):
        if self.comodin == 1:
            letra = random.choice([l for l in self.palabra if l not in self.letras_adivinadas])
            self.ingresar_letra(letra)
            self.comodin = 0
            return letra
        return None