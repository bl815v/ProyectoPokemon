from Logic.Pokemon.Tipos import PokemonElectrico

class Pikachu(PokemonElectrico):
    def __init__(self, tipo, nombre, vida, ataque, defensa, debilidad, resistencia):
        super().__init__(nombre, vida, ataque, defensa, debilidad, resistencia)
        self._tipo = "Electrico"
        self._nombre = "Pikachu"
        self._vida = 95
        self._ataque = 50
        self._defensa = 40
        self._debilidad = "Roca"
        self._resitencia = "Electrico"