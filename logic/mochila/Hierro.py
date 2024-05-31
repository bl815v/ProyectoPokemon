from logic.mochila.Objetos import Objetos

class Hierro(Objetos):
    """Clase que se encarga de representar el objeto Hierro.
     
    Args:

    Attributes:
        nombre: nombre del objeto.
        Ps: Ps del objeto.
        PP: PP del objeto.
        Ataque: ataque del objeto.
        Defensa: defensa del objeto.
        Cantidad: cantidad disponible del objeto.
    
       """
    def __init__(self, nombre, PS, PP, ataque, defensa, cantidad):
        super().__init__(nombre, PS, PP, ataque, defensa, cantidad)
        """Inicializa la clase Hierro.
        Args:
        nombre: nombre del objeto.
        Ps: Ps del objeto.
        PP: PP del objeto.
        Ataque: ataque del objeto.
        Defensa: defensa del objeto.
        Cantidad: cantidad disponible del objeto.
            
        """
        self._nombre = "Hierro"
        self._PS = 20
        self._PP = 0
        self._ataque = 0
        self._defensa = 20
        self._cantidad = 2