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

    return jsonify({
        "message": "Nueva palabra configurada. ¡Comienza el juego!",
        "palabra": juego_actual.muestra_palabra(),  # Mostrar los '____'
        "vidas": juego_actual.vidas,
        "erradas": []
    })

@app.route('/ingresar_letra', methods=['POST'])
def ingresar_letra():
    global juego_actual
    letra = request.form['letra'].lower()
    resultado = juego_actual.ingresar_letra(letra)
    fin_juego = juego_actual.comprueba_fin_de_juego()

    if fin_juego:
        juego_actual = None
        return jsonify({
            "acierto": resultado,
            "fin_juego": fin_juego,
            "reiniciar": True
        })
    
    return jsonify({
        "acierto": resultado,
        "vidas": juego_actual.vidas,
        "palabra": juego_actual.muestra_palabra(),
        "erradas": juego_actual.muestra_letras_erradas(),
        "fin_juego": fin_juego,
        "reiniciar": False
    })

@app.route('/arriesgar_palabra', methods=['POST'])
def arriesgar_palabra():
    global juego_actual
    palabra_ingresada = request.form['palabra_arriesga']
    resultado = juego_actual.arriesgar_palabra(palabra_ingresada)
    fin_juego = juego_actual.comprueba_fin_de_juego()

    palabra_mostrada = juego_actual.muestra_palabra()

    if fin_juego:
        juego_actual = None
        return jsonify({
            "resultado": resultado,
            "palabra": palabra_mostrada,
            "fin_juego": fin_juego,
            "reiniciar": True
        })

    return jsonify({
        "resultado": resultado,
        "palabra": palabra_mostrada,
        "vidas": juego_actual.vidas,
        "fin_juego": fin_juego,
        "reiniciar": False
    })

@app.route('/usar_comodin', methods=['POST'])
def usar_comodin():
    letra_comodin = juego_actual.uso_comodin()
    return jsonify({
        "letra_comodin": letra_comodin,
        "vidas": juego_actual.vidas,
        "palabra": juego_actual.muestra_palabra(),
        "erradas": juego_actual.muestra_letras_erradas(),
        "fin_juego": juego_actual.comprueba_fin_de_juego()
    })


@app.route('/reiniciar', methods=['POST'])
def reiniciar():
    global juego_actual
    juego_actual = Ahorcado("python")
    return jsonify({"message": "Juego reiniciado."})

if __name__ == '__main__':
    app.run(debug=True)