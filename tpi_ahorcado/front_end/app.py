from flask import Flask, request, jsonify
from tpi_ahorcado.Ahorcado import Ahorcado

app = Flask(__name__)

# Instancia global del juego
juego = None

@app.route('/iniciar', methods=['POST'])
def iniciar_juego():
    global juego
    data = request.json
    palabra = data.get('palabra')
    if not palabra:
        return jsonify({'error': 'Se debe proporcionar una palabra para iniciar el juego'}), 400
    juego = Ahorcado(palabra)
    return jsonify({'mensaje': 'Juego iniciado', 'vidas': juego.vidas, 'estado': juego.muestra_palabra()})

@app.route('/estado', methods=['GET'])
def obtener_estado():
    if not juego:
        return jsonify({'error': 'El juego no ha iniciado'}), 400
    return jsonify({
        'palabra': juego.muestra_palabra(),
        'vidas': juego.vidas,
        'letras_erradas': juego.muestra_letras_erradas(),
        'fin_de_juego': juego.fin_de_juego
    })

@app.route('/adivinar', methods=['POST'])
def adivinar():
    if not juego:
        return jsonify({'error': 'El juego no ha iniciado'}), 400
    data = request.json
    letra = data.get('letra')
    if not letra or len(letra) != 1:
        return jsonify({'error': 'Debe ingresar una letra válida'}), 400
    resultado = juego.ingresar_letra(letra)
    return jsonify({
        'resultado': 'acertó' if resultado else 'falló',
        'estado': juego.muestra_palabra(),
        'vidas': juego.vidas,
        'letras_erradas': juego.muestra_letras_erradas(),
        'fin_de_juego': juego.fin_de_juego
    })

@app.route('/comodin', methods=['POST'])
def usar_comodin():
    if not juego:
        return jsonify({'error': 'El juego no ha iniciado'}), 400
    resultado = juego.uso_comodin()
    return jsonify({
        'resultado': 'usado' if resultado else 'no disponible',
        'estado': juego.muestra_palabra(),
        'vidas': juego.vidas
    })

if __name__ == '__main__':
    app.run(debug=True)
