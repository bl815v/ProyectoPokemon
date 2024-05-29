from Logic.Pokemon.DiccionarioPokemon import DiccionarioPokemon
from Logic.Pokemon.DiccionarioObjetos import DiccionarioObjetos
from Logic.Movimientos.ListaMovimiento import ListaMovimiento
from Logic.combate.Juego import Juego
import random

print(DiccionarioObjetos().DiccionarioDeObjetos('Hierro', 'Todo'))  #Escribe el nombre del objeto y el tipo de estadistica que necesita- si son todas las estadisticas 'Todo'
print(DiccionarioPokemon().DiccionarioDePokemon('Pikachu', 'Todo'))   #Escribe el nombre del pokemon y el tipo de estadistica que necesita- si son todas 'Todo'

print(ListaMovimiento().crearMovimientos(0))    #Solo para obtener la lista que contiene todas la informacion de un movimiento
print(ListaMovimiento().IdentifMovsPokemon('Bulbasaur'))    #Obtiene la lista con los 4 ataques y toda su informacion

print(ListaMovimiento().EstadisticasMovimientos('Pikachu', 2,'Nombre'))   #Esta seria la ideal para usar, escribe el nombre del pokemon que necesita, el numero del ataque (1-4), y 
                                                                        #especificamente lo que necesita- si son todas las estadisticas 'Todo'

#print(Juego().batalla())
print(Juego().UsarObjetoUsuario("Eter"))
aleatorio = random.random()
print(aleatorio)
