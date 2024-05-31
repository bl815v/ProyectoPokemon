from abc import ABC
import random

class PokemonBase(ABC):
    """Clase que se encarga de crear el pokemon abstracto.
     
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
        """Inicializa PokemonBase con los argumentos.
     
        Args:
            tipo: String que representa el tipo de pokemon.
            nombre: String que representa el nombre del pokemon.
            vida: Int que representa la vida total del pokemon.
            ataque: Int que representa el ataque del pokemon.
            defensa: Int que representa la defensa del pokemon.
            debilidad: Lista de strings que representa la o las debilidades del pokemon.
            resistencia: Lista de strings que representa la o las resistencias del pokemon.        
       """
        self._tipo = tipo
        self._nombre = nombre
        self._vida = vida
        self._ataque = ataque
        self._defensa = defensa
        self._debilidad = debilidad
        self._resitencia = resistencia
    
    def getTipo(self):
        """Devuelve el valor contenido en _tipo.

        Returns:
            _tipo: String que representa el tipo de pokemon.
        """
        return self._tipo
    
    def setTipo(self,tipo):
        """Establece el valor que contiene _tipo.

        Args:
            tipo: String que representa el tipo de pokemon.
        """
        self._tipo = tipo

    def getNombre(self):
        """Devuelve el valor contenido en _nombre.

        Returns:
            _nombre: String que representa el nombre del pokemon.
        """
        return self._nombre
    
    def setNombre(self,nombre):
        """Establece el valor que contiene _nombre.

        Args:
            nombre: String que representa el tipo de pokemon.
        """
        self._nombre = nombre
        
    def getVida(self):
        """Devuelve el valor contenido en _vida.

        Returns:
            _vida: Int que representa la vida total del pokemon.
        """
        return self._vida
    
    def setVida(self,vida):
        """Establece el valor que contiene _vida.

        Args:
            vida: Int que representa la vida total del pokemon.
        """
        self._vida = vida
        
    def getAtaque(self):
        """Devuelve el valor contenido en _ataque.

        Returns:
            _ataque: Int que representa el ataque del pokemon.
        """
        return self._ataque
    
    def setAtaque(self,ataque):
        """Establece el valor que contiene _ataque.

        Args:
            ataque: Int que representa el ataque del pokemon.
        """
        self._ataque = ataque
        
    def getDefensa(self):
        """Devuelve el valor contenido en _defensa.

        Returns:
            _defensa: Int que representa la defensa del pokemon.
        """
        return self._defensa
    
    def setDefensa(self,defensa):
        """Establece el valor que contiene _defensa.

        Args:
            defensa: Int que representa la defensa del pokemon.
        """
        self._defensa = defensa
        
    def getDebilidad(self):
        """Devuelve el valor contenido en _debilidad.

        Returns:
            _debilidad: Lista de strings que representa la o las debilidades del pokemon.
        """
        return self._debilidad
    
    def setDebilidad(self,debilidad):
        """Establece el valor que contiene _debilidad.

        Args:
            debilidad: Lista de strings que representa la o las debilidades del pokemon.
        """
        self._debilidad = debilidad
    
    def getResistencia(self):
        """Devuelve el valor contenido en _resistencia.

        Returns:
            _resistencia: Lista de strings que representa la o las resistencias del pokemon.
        """
        return self._resitencia
    
    def setResistencia(self,resistencia):
        """Establece el valor que contiene _resistencia.

        Args:
            resistencia: Lista de strings que representa la o las resistencias del pokemon.
        """
        self._resistencia = resistencia  

    def CalcDaño(self, potenciaAtaque, ataquePropio, defensaRival):
        """Calcula el daño que un pokemon le inflinge al otro.
        Args:
            potenciaAtaque: Potencia del ataque en uso.
            ataquePropio: Valor del ataque del pokemon que va atacar.
            defensaRival: Valor de la defensa del rival.

        Returns:
            resultado: Devuelve el resultado de la operacion multiplicado con un numero aleatorio.
        """
        numero_aleatorio = random.uniform(0.85, 1.0)
        resultado = (((((2*50)/5)+2 * potenciaAtaque * (ataquePropio/defensaRival)) / 50) + 2)
        return resultado * numero_aleatorio

    def getPropiedades(self):
        """Devuelve todas los atributos del pokemon en uso.

        Returns:
            _tipo: String que representa el tipo de pokemon.
            _nombre: Sttring que representa el nombre del pokemon.
            _vida: Int que representa la vida total del pokemon.
            _ataque: Int que representa el ataque del pokemon.
            _defensa: Int que representa la defensa del pokemon.
            _debilidad: Lista de strings que representa la o las debilidades del pokemon.
            _resistencia: Lista de strings que representa la o las resistencias del pokemon.
        """
        return (self._nombre, self._tipo, self._vida, self._ataque, self._defensa, self._debilidad, self._resistencia)