from logic.pokemon.PokemonBase import PokemonBase

class PokemonBicho(PokemonBase):
    """Clase que se encarga de crear el tipo de pokemon de bicho.
     
    Args:
        tipo: String que representa el tipo de pokemon.
        nombre: String que representa el nombre del pokemon.
        vida: Int que representa la vida total del pokemon.
        ataque: Int que representa el ataque del pokemon.
        defensa: Int que representa la defensa del pokemon.
        debilidad: Lista de strings que representa la o las debilidades del pokemon.
        resistencia: Lista de strings que representa la o las resistencias del pokemon.

    Attributes:
        _tipo: String que representa el tipo de pokemon.
        _nombre: Sttring que representa el nombre del pokemon.
        _vida: Int que representa la vida total del pokemon.
        _ataque: Int que representa el ataque del pokemon.
        _defensa: Int que representa la defensa del pokemon.
        _debilidad: Lista de strings que representa la o las debilidades del pokemon.
        _resistencia: Lista de strings que representa la o las resistencias del pokemon.
    
       """
    def __init__(self, tipo, nombre, vida,ataque,defensa, debilidad, resistencia):
        """Inicializa PokemonBicho con los argumentos.
     
        Args:
            tipo: String que representa el tipo de pokemon.
            nombre: String que representa el nombre del pokemon.
            vida: Int que representa la vida total del pokemon.
            ataque: Int que representa el ataque del pokemon.
            defensa: Int que representa la defensa del pokemon.
            debilidad: Lista de strings que representa la o las debilidades del pokemon.
            resistencia: Lista de strings que representa la o las resistencias del pokemon.        
       """
        super().__init__(tipo, nombre, vida,ataque,defensa, debilidad, resistencia)
        