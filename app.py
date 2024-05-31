from flask import Flask, render_template, request, send_from_directory
from flask_mysqldb import MySQL

from data.Admin_base import Admin_base
from logic.Estilo import Estilo
from logic.Usuario import Usuario
from logic.combate.Juego import Juego

app=Flask(__name__, template_folder='web/template', static_folder='web/static')
app.secret_key = 'clave'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '151709Jebl'
app.config['MYSQL_DB'] = 'batallasPokemon'

mysql = MySQL(app)

admin_base = Admin_base(mysql)

@app.route('/usuarios')
def usuarios():    
    usuarios = admin_base.getUsuarios()
    return render_template('usuarios.html', usuarios=usuarios)


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

@app.route('/RegistroExitoso', methods=['POST'])
def RegistroExitoso():
    nombre = request.form.get('nombre')
    correo = request.form.get('correo')
    clave = request.form.get('clave')
    repetirclave = request.form.get('repetirclave')

    if clave != repetirclave:
        return "Las contraseñas no coinciden. Inténtalo de nuevo."

    nuevo_usuario = Usuario(nombre, correo, clave)

    admin_base.guardarUsuario(nuevo_usuario)
    background_url = Estilo.obtener_fondo_gif('inicial')
    return render_template('index.html', background_url=background_url)

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
    Iniciarjuego = Juego()
    background_url = Estilo.obtener_fondo_png('batalla')
    return render_template('batalla.html', background_url=background_url)


if __name__ == '__main__':
    app.run(debug=True, port=5000)