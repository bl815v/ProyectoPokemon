from Logic.Mochila import Objetos

class BolaLodo(Objetos):
    def __init__(self, nombre, PS, PP, ataque, defensa, cantidad):
        super().__init__(nombre, PS, PP, ataque, defensa, cantidad)
        self._nombre = "BolaLodo"
        self._PS = 0
        self._PP = 0
        self._ataque = -20
        self._defensa = 0
        self._cantidad = 2