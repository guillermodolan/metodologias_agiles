from Ahorcado import Ahorcado

palabra_correcta = input('Ingrese la palabra correcta: ')
ahorcado = Ahorcado(palabra_correcta)

FIN_JUEGO = False

while not FIN_JUEGO and ahorcado.vidas > 0:
    letra = input('Ingresá una letra: ')
    ahorcado.ingresar_letra(letra)
    print(ahorcado.muestra_palabra())
    if not '_' in ahorcado.muestra_palabra():
        FIN_JUEGO = True
if Ahorcado.vidas != 0:
    print('Fin del juego, ganaste')
else:
    print('Perdiste')