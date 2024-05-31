from flask import Flask, render_template, send_from_directory, url_for

from logic.Estilo import Estilo

app=Flask(__name__, template_folder='web/template', static_folder='web/static')
app.secret_key = 'clave'


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    background_url = Estilo.obtener_fondo_gif('inicial')
    return render_template('index.html', background_url=background_url)

@app.route('/registro')
def registro():
    background_url = Estilo.obtener_fondo_gif('inicial')
    return render_template('registro.html', background_url=background_url)

@app.route('/usuario')
def usuario():
    background_url = Estilo.obtener_fondo_gif('menu')
    return render_template('usuario.html', background_url=background_url)

@app.route('/ganaste')
def ganaste():
    background_url = Estilo.obtener_fondo_gif('ganaste')
    return render_template('ganaste.html', background_url=background_url)


@app.route('/perdiste')
def perdiste():
    background_url = Estilo.obtener_fondo_gif('perdiste')
    return render_template('perdiste.html', background_url=background_url)

@app.route('/batalla')
def batalla():
    background_url = Estilo.obtener_fondo_png('batalla')
    return render_template('batalla.html', background_url=background_url)


if __name__ == '__main__':
    app.run(debug=True, port=5000)