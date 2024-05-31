from logic.mochila.Objetos import Objetos

class Eter(Objetos):
    """Clase que se encarga de representar el objeto Eter.
     
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
        """Inicializa la clase Eter.
        Args:
        nombre: nombre del objeto.
        Ps: Ps del objeto.
        PP: PP del objeto.
        Ataque: ataque del objeto.
        Defensa: defensa del objeto.
        Cantidad: cantidad disponible del objeto.
            
        """
        self._nombre = "Eter"
        self._PS = 0
        self._PP = 1
        self._ataque = 0
        self._defensa = 0
        self._cantidad = 3