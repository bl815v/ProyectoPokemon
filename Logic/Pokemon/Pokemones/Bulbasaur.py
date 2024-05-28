from Logic.Pokemon.Tipos.PokemonPlanta import PokemonPlanta
from Logic.Movimientos.ListaMovimiento import ListaMovimiento

class Bulbasaur(PokemonPlanta):
    def __init__(self, tipo, nombre, vida, ataque, defensa, debilidad, resistencia):
        super().__init__(tipo, nombre, vida, ataque, defensa, debilidad, resistencia)
        self._tipo = "Planta"
        self._nombre = "Bulbasaur"
        self._vida = 105
        self._ataque = 50
        self._defensa = 50
        self._debilidad = ["Fuego"]
        self._resistencia = ["Agua", "Planta", "Electrico"]