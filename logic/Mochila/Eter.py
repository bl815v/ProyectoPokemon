from Logic.Mochila.Objetos import Objetos

class Eter(Objetos):
    def __init__(self, nombre, PS, PP, ataque, defensa, cantidad):
        super().__init__(nombre, PS, PP, ataque, defensa, cantidad)
        self._nombre = "Eter"
        self._PS = 0
        self._PP = 1
        self._ataque = 0
        self._defensa = 0
        self._cantidad = 3