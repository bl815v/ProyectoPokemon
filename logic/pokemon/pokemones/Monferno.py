from Logic.Pokemon.Tipos.PokemonFuego import PokemonFuego

class Monferno(PokemonFuego):
    def __init__(self, tipo, nombre, vida, ataque, defensa, debilidad, resistencia):
        super().__init__(tipo, nombre, vida, ataque, defensa, debilidad, resistencia)
        self._tipo = "Fuego"
        self._nombre = "Monferno"
        self._vida = 125
        self._ataque = 75
        self._defensa = 50
        self._debilidad = ["Agua"]
        self._resistencia = ["Planta", "Fuego", "Bicho"]