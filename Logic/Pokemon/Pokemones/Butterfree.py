from Logic.Pokemon.Tipos.PokemonBicho import PokemonBicho

class Butterfree(PokemonBicho):
    def __init__(self, tipo, nombre, vida, ataque, defensa, debilidad, resistencia):
        super().__init__(tipo, nombre, vida, ataque, defensa, debilidad, resistencia)
        self._tipo = "Bicho"
        self._nombre = "Butterfree"
        self._vida = 120
        self._ataque = 45
        self._defensa = 50
        self._debilidad = ["Fuego"]
        self._resistencia = ["Bicho", "Planta"]