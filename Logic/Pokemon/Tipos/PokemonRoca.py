from Logic.Pokemon import Pokemon

class PokemonRoca(Pokemon):
    def __init__(self, tipo, nombre, vida,ataque,defensa, debilidad, resistencia):
        super().__init__(tipo, nombre, vida,ataque,defensa, debilidad, resistencia)
        