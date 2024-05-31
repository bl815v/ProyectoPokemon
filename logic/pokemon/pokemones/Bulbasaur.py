from logic.pokemon.tipos.PokemonPlanta import PokemonPlanta

class Bulbasaur(PokemonPlanta):
    """Clase que se encarga de crear el pokemon Bulbasaur.
     
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
    def __init__(self, tipo, nombre, vida, ataque, defensa, debilidad, resistencia):
        """Inicializa Bulbasaur con los argumentos.
     
        Args:
            tipo: String que representa el tipo de pokemon.
            nombre: String que representa el nombre del pokemon.
            vida: Int que representa la vida total del pokemon.
            ataque: Int que representa el ataque del pokemon.
            defensa: Int que representa la defensa del pokemon.
            debilidad: Lista de strings que representa la o las debilidades del pokemon.
            resistencia: Lista de strings que representa la o las resistencias del pokemon.        
       """
        super().__init__(tipo, nombre, vida, ataque, defensa, debilidad, resistencia)
        self._tipo = "Planta"
        self._nombre = "Bulbasaur"
        self._vida = 105
        self._ataque = 50
        self._defensa = 50
        self._debilidad = ["Fuego"]
        self._resistencia = ["Agua", "Planta", "Electrico"]