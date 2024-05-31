from Logic.Pokemon.Tipos.PokemonAgua import PokemonAgua

class Vaporeon(PokemonAgua):
    def __init__(self, tipo, nombre, vida, ataque, defensa, debilidad, resistencia):
        super().__init__(tipo, nombre, vida, ataque, defensa, debilidad, resistencia)
        self._tipo = "Agua"
        self._nombre = "Vaporeon"
        self._vida = 190
        self._ataque = 63
        self._defensa = 60
        self._debilidad = ["Electrico", "Planta"]
        self._resistencia = ["Agua", "Fuego"]