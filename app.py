from flask import Flask, render_template, request, jsonify
from Ahorcado import Ahorcado

app = Flask(__name__)

juego_actual = Ahorcado("python")

@app.route('/')
def index():
    return render_template('index.html', vidas=juego_actual.vidas, palabra=juego_actual.muestra_palabra(), erradas=juego_actual.muestra_letras_erradas())

@app.route('/configurar_palabra', methods=['POST'])
def configurar_palabra():
    global juego_actual
    palabra = request.form['palabra']
    juego_actual = Ahorcado(palabra)
    return jsonify({"message": "Palabra configurada correctamente."})

@app.route('/ingresar_letra', methods=['POST'])
def ingresar_letra():
    letra = request.form['letra']
    resultado = juego_actual.ingresar_letra(letra)
    fin_juego = juego_actual.comprueba_fin_de_juego()
    return jsonify({
        "acierto": resultado,
        "vidas": juego_actual.vidas,
        "palabra": juego_actual.muestra_palabra(),
        "erradas": juego_actual.muestra_letras_erradas(),
        "fin_juego": fin_juego
    })

@app.route('/arriesgar_palabra', methods=['POST'])
def arriesgar_palabra():
    palabra_ingresada = request.form['palabra_arriesga']
    print(f'Palabra ingresada: {palabra_ingresada}')
    resultado = juego_actual.arriesgar_palabra(palabra_ingresada)
    fin_juego = juego_actual.comprueba_fin_de_juego()
    return jsonify({
        "resultado": resultado,
        "vidas": juego_actual.vidas,
        "fin_juego": fin_juego
    })

@app.route('/reiniciar', methods=['POST'])
def reiniciar():
    global juego_actual
    juego_actual = Ahorcado("python")
    return jsonify({"message": "Juego reiniciado."})

if __name__ == '__main__':
    app.run(debug=True)