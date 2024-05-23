from Logic.Pokemon.Tipos import PokemonRoca

class Sudowoodo(PokemonRoca):
    def __init__(self, tipo, nombre, vida, ataque, defensa, debilidad, resistencia):
        super().__init__(tipo, nombre, vida, ataque, defensa, debilidad, resistencia)
        self._tipo = "Roca"
        self._nombre = "Sudowoodo"
        self._vida = 130
        self._ataque = 90
        self._defensa = 100
        self._debilidad = ["Agua", "Planta"]
        self._resitencia = ["Electrico", "Fuego"]