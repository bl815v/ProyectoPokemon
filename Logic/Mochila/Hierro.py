from Logic.Mochila import Objetos

class Hierro(Objetos):
    def __init__(self, nombre, PS, PP, ataque, defensa, cantidad):
        super().__init__(nombre, PS, PP, ataque, defensa, cantidad)
        self._nombre = "Hierro"
        self._PS = 20
        self._PP = 0
        self._ataque = 0
        self._defensa = 20
        self._cantidad = 2