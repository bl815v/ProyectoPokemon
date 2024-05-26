from Logic.Pokemon.PokemonBase import Pokemon

class PokemonBicho(Pokemon):
    def __init__(self, tipo, nombre, vida,ataque,defensa, debilidad, resistencia):
        super().__init__(tipo, nombre, vida,ataque,defensa, debilidad, resistencia)
        