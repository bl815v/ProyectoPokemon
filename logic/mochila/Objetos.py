from abc import ABC

class Objetos(ABC):
    """Clase abstraci¿ta que se encarga de representar los objetos que puede usar un jugador.
     
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
        """Inicializa la clase.
        Args:
        nombre: nombre del objeto.
        Ps: Ps del objeto.
        PP: PP del objeto.
        Ataque: ataque del objeto.
        Defensa: defensa del objeto.
        Cantidad: cantidad disponible del objeto.
            
        """
        self._nombre = nombre
        self._PS = PS
        self._PP = PP
        self._ataque = ataque
        self._defensa = defensa
        self._cantidad = cantidad
    
    def getNombre(self):
        """Obtiene el nombre del objeto.
        
        Returns:
            nombre del objeto.
        """
        return self._nombre
    
    def setNombre(self,nombre):
        """Define la resistencia del pokemon del pc.
        Args:
            resistencia (Int): resistencia del pokemon del pc.
        """
        self._nombre = nombre
        
    def getPS(self):
        """Obtiene el ps del objeto.
        
        Returns:
            ps del objeto.
        """
        return self._PS
    
    def setPS(self,PS):
        """Define el ps del objeto.
        Args:
            ps (Int): ps del objeto.
        """
        self._PS = PS
    
    def getPP(self):
        """Obtiene el pp del objeto.
        
        Returns:
            pp del objeto.
        """
        return self._PP
    
    def setPP(self,PP):
        """Define el pp del objeto.
        Args:
            pp (Int): pp del objeto.
        """
        self._PP = PP

    def getAtaque(self):
        """Obtiene el ataque del objeto.
        
        Returns:
            ataque del objeto.
        """
        return self._ataque
    
    def setAtaque(self,ataque):
        """Define el ataque del objeto.
        Args:
            ataque (Int): ataque del objeto.
        """
        self._ataque = ataque
        
    def getDefensa(self):
        """Obtiene la defensa del objeto.
        
        Returns:
            defensa del objeto.
        """
        return self._defensa
    
    def setDefensa(self,defensa):
        """Define el defensa del objeto.
        Args:
            defensa (Int): defensa del objeto.
        """
        self._defensa = defensa

    def getCantidad(self):
        """Obtiene la cantidad del objeto.
        
        Returns:
            cantidad del objeto.
        """
        return self._cantidad
    
    def setCantidad(self, cantidad):
        """Define la cantidad del objeto.
        Args:
            cantidad (Int): cantidad del objeto.
        """
        self._cantidad = cantidad

    def getPropiedades(self):
        """Obtiene las propiedades del objeto.
        
        Returns:
            propiedades del objeto.
        """
        return (self._nombre, self._PS, self._PP, self._ataque, self._defensa, self._cantidad)
        