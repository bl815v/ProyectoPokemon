from Logic.Pokemon import Pokemon

class PokemonRoca(Pokemon):
    def __init__(self, nombre, vida,ataque,defensa, debilidad, resistencia):
        super().__init__(nombre, vida,ataque,defensa, debilidad, resistencia)
        