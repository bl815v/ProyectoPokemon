from Logic.Pokemon.Tipos import PokemonFuego

class Charmander(PokemonFuego):
    def __init__(self, tipo, nombre, vida, ataque, defensa, debilidad, resistencia):
        super().__init__(tipo, nombre, vida, ataque, defensa, debilidad, resistencia)
        self._tipo = "Fuego"
        self._nombre = "Charmander"
        self._vida = 100
        self._ataque = 50
        self._defensa = 40
        self._debilidad = ["Agua"]
        self._resitencia = ["Planta", "Fuego"]