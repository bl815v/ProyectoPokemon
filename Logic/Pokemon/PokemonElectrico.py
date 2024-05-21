from Pokemon.Logic.Pokemon import Pokemon

class PokemonElectrico(Pokemon):
    def __init__(nombre, vida,ataque,defensa, debilidad, resistencia):
        super().__init__(nombre, vida,ataque,defensa, debilidad, resistencia)
        