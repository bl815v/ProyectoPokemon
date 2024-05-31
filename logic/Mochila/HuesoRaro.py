from Logic.Mochila.Objetos import Objetos

class HuesoRaro(Objetos):
    def __init__(self, nombre, PS, PP, ataque, defensa, cantidad):
        super().__init__(nombre, PS, PP, ataque, defensa, cantidad)
        self._nombre = "HuesoRaro"
        self._PS = 0
        self._PP = 0
        self._ataque = 0
        self._defensa = -20
        self._cantidad = 2