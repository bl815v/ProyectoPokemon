import os
import random
from flask import url_for

class Estilo:

    @staticmethod
    def obtener_fondo_gif(carpeta):
        backgrounds_path = os.path.join('web/static', 'fondo', carpeta)
        gifs = [f for f in os.listdir(backgrounds_path) if f.endswith('.gif')]
        selected_gif = random.choice(gifs)
        background_url = url_for('static', filename=f'fondo/{carpeta}/{selected_gif}')
        return background_url
    
    @staticmethod
    def obtener_fondo_png(carpeta):

        backgrounds_path = os.path.join('web/static', 'fondo', carpeta)
        png = [f for f in os.listdir(backgrounds_path) if f.endswith('.png')]
        selected_png = random.choice(png)
        background_url = url_for('static', filename=f'fondo/{carpeta}/{selected_png}')
        return background_url