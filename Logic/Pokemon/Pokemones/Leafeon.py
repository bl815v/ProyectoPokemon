from Logic.Pokemon.Tipos import PokemonPlanta

class Leafeon(PokemonPlanta):
    def __init__(self, tipo, nombre, vida, ataque, defensa, debilidad, resistencia):
        super().__init__(tipo, nombre, vida, ataque, defensa, debilidad, resistencia)
        self._tipo = "Planta"
        self._nombre = "Leafeon"
        self._vida = 125
        self._ataque = 100
        self._defensa = 120
        self._debilidad = ["Fuego", "Bicho"]
        self._resitencia = ["Agua", "Planta", "Electrico"]