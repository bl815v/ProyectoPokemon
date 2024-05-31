from abc import ABC

class Objetos(ABC):
    def __init__(self, nombre, PS, PP, ataque, defensa, cantidad):
        self._nombre = nombre
        self._PS = PS
        self._PP = PP
        self._ataque = ataque
        self._defensa = defensa
        self._cantidad = cantidad
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self,nombre):
        self._nombre = nombre
        
    def getPS(self):
        return self._PS
    
    def setPS(self,PS):
        self._PS = PS
    
    def getPP(self):
        return self._PP
    
    def setPP(self,PP):
        self._PP = PP

    def getAtaque(self):
        return self._ataque
    
    def setAtaque(self,ataque):
        self._ataque = ataque
        
    def getDefensa(self):
        return self._defensa
    
    def setDefensa(self,defensa):
        self._defensa = defensa

    def getCantidad(self):
        return self._cantidad
    
    def setCantidad(self, cantidad):
        self._cantidad = cantidad

    def getPropiedades(self):
        return (self._nombre, self._PS, self._PP, self._ataque, self._defensa, self._cantidad)
        