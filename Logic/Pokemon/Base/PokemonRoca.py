from Logic.Pokemon.Base import Pokemon

class PokemonRoca(Pokemon):
    def __init__(nombre, vida,ataque,defensa, debilidad, resistencia):
        super().__init__(nombre, vida,ataque,defensa, debilidad, resistencia)
        