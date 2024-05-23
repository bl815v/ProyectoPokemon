from abc import ABC
import random

class Pokemon(ABC):
    def __init__(self, nombre, vida, ataque, defensa, debilidad, resistencia):
        self._nombre = nombre
        self._vida = vida
        self._ataque = ataque
        self._defensa = defensa
        self._debilidad = debilidad
        self._resitencia = resistencia
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self,nombre):
        self._nombre = nombre
        
    def getVida(self):
        return self._vida
    
    def setVida(self,vida):
        self._vida = vida
        
    def getAtaque(self):
        return self._ataque
    
    def setAtaque(self,ataque):
        self._ataque = ataque
        
    def getDefensa(self):
        return self._defensa
    
    def setDefensa(self,defensa):
        self._defensa = defensa
        
    def getDebilidad(self):
        return self._debilidad
    
    def setDebilidad(self,debilidad):
        self._debilidad = debilidad
    
    def getResistencia(self):
        return self._resitencia
    
    def setResistencia(self,resistencia):
        self._resistencia = resistencia  

    def CalcDaño(self, potenciaAtaque, ataquePropio, defensaRival):
        numero_aleatorio = random.uniform(0.85, 1.0)
        resultado = (((((2*50)/5)+2 * potenciaAtaque * (ataquePropio/defensaRival)) / 50) + 2)
        return resultado * numero_aleatorio
    
    def UsarObjeto(self, PS, PP, ataque, defensa):
        pass