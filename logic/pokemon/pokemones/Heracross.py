from Logic.Pokemon.Tipos.PokemonBicho import PokemonBicho

class Heracross(PokemonBicho):
    def __init__(self, tipo, nombre, vida, ataque, defensa, debilidad, resistencia):
        super().__init__(tipo, nombre, vida, ataque, defensa, debilidad, resistencia)
        self._tipo = "Bicho"
        self._nombre = "Heracross"
        self._vida = 140
        self._ataque = 110
        self._defensa = 70
        self._debilidad = ["Fuego"]
        self._resistencia = ["Bicho", "Planta"]