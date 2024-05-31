from Logic.Pokemon.Tipos import PokemonAgua

class Squirtle(PokemonAgua):
    def __init__(self, tipo, nombre, vida, ataque, defensa, debilidad, resistencia):
        super().__init__(tipo, nombre, vida, ataque, defensa, debilidad, resistencia)
        self._tipo = "Agua"
        self._nombre = "Squirtle"
        self._vida = 100
        self._ataque = 45
        self._defensa = 60
        self._debilidad = ["Electrico", "Planta"]
        self._resitencia = ["Agua", "Fuego"]