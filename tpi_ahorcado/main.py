from Ahorcado import Ahorcado

palabra_correcta = input('Ingrese la palabra correcta: ')
ahorcado = Ahorcado(palabra_correcta)

fin_juego = False

while not fin_juego and Ahorcado.vidas > 0:
    letra = input('Ingresá una letra: ')
    ahorcado.ingresar_letra(letra)
    print(ahorcado.muestra_palabra())
    if not '_' in ahorcado.muestra_palabra():
        fin_juego = True
        
if Ahorcado.vidas != 0:
    print('Fin del juego, ganaste')
else:
    print('Perdiste')
