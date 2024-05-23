from Logic.Pokemon.Tipos import PokemonRoca

class Onix(PokemonRoca):
    def __init__(self, tipo, nombre, vida, ataque, defensa, debilidad, resistencia):
        super().__init__(tipo, nombre, vida, ataque, defensa, debilidad, resistencia)
        self._tipo = "Roca"
        self._nombre = "Onix"
        self._vida = 95
        self._ataque = 50
        self._defensa = 140
        self._debilidad = ["Agua", "Planta"]
        self._resitencia = ["Fuego"]