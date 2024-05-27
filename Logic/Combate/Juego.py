from Logic.Pokemon.DiccionarioPokemon import DiccionarioPokemon
import random

class Juego():
    def elegirPokemones():
        numero1 = random.randint(1, 12) #genera un numero aleatorio del 1 al 12
        
        while(True):
            numero2 = random.randint(1, 12)
            if numero2 != numero1:  #genera un numero aleatorio y garantiza que no sea el mismo que el a¿otro numero generado
                break

        
            