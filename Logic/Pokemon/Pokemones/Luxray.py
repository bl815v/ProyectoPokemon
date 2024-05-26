from Logic.Pokemon.Tipos.PokemonElectrico import PokemonElectrico

class Luxray(PokemonElectrico):
    def __init__(self, tipo, nombre, vida, ataque, defensa, debilidad, resistencia):
        super().__init__(tipo, nombre, vida, ataque, defensa, debilidad, resistencia)
        self._tipo = "Electrico"
        self._nombre = "Luxray"
        self._vida = 140
        self._ataque = 110
        self._defensa = 75
        self._debilidad = ["Roca"]
        self._resistencia = ["Electrico"]