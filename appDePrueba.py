from Logic.Pokemon.DiccionarioPokemon import DiccionarioPokemon
from Logic.Pokemon.DiccionarioObjetos import DiccionarioObjetos
from Logic.Movimientos.ListaMovimiento import ListaMovimiento
from Logic.combate.Juego import Juego
import random

#print(DiccionarioObjetos().DiccionarioDeObjetos('Hierro', 'Todo'))  #Escribe el nombre del objeto y el tipo de estadistica que necesita- si son todas las estadisticas 'Todo'
#print(DiccionarioPokemon().DiccionarioDePokemon('Pikachu', 'Todo'))   #Escribe el nombre del pokemon y el tipo de estadistica que necesita- si son todas 'Todo'

#print(ListaMovimiento().crearMovimientos(0))    #Solo para obtener la lista que contiene todas la informacion de un movimiento
#print(ListaMovimiento().IdentifMovsPokemon('Bulbasaur'))    #Obtiene la lista con los 4 ataques y toda su informacion

#print(ListaMovimiento().EstadisticasMovimientos('Pikachu', 3,'Nombre'))   #Esta seria la ideal para usar, escribe el nombre del pokemon que necesita, el numero del ataque (1-4), y 
                                                                        #especificamente lo que necesita- si son todas las estadisticas 'Todo'
#print(Juego().movimientosPokemonUser[0][4])

#print(Juego().AumentarPpMovimiento('User',-1))

#print(Juego().batalla(0, 0, 'BolaLodo'))
#print(Juego().UsarObjetoUsuario("Eter"))
#print(Juego().getVidaPokemon_user())

def EscribirEstats():
    print('Pokemon rival', Juego()._pokemon_pc , ' ' , Juego().vidaPokemonPc , ' ' ,
    Juego().vidaTotalPc , ' ' ,
    Juego().ataquePokemonPc  , ' ' ,
    Juego().defensaPokemonPc , ' ' ,
    Juego().tipoPokemonPc , ' ' ,
    Juego().debilidadPokemonPc , ' ' ,
    Juego().resistenciaPokemonPc , ' ' ,
    Juego().movimientosPokemonPc , ' ' ,
    Juego().movimientosPPMaximosPc)

    print('\nPokemon jugador: ' , Juego()._pokemon_user , ' ' , Juego().vidaPokemonUser , ' ' ,
    Juego().vidaTotalUser , ' ' ,
    Juego().ataquePokemonUser , ' ' ,
    Juego().defensaPokemonUser , ' ' ,
    Juego().tipoPokemonUser , ' ' ,
    Juego().debilidadPokemonUser , ' ' ,
    Juego().resistenciaPokemonUser , ' ' ,
    Juego().movimientosPokemonUser , ' ' ,
    Juego().movimientosPPMaximosUser)

Juego().elegirPokemones()
EscribirEstats()

FinPartida = 0
i = 1
while(FinPartida == 0):
    if i == 3:
        i = 1
    
    intencion = input('\n1 es ataque, 0 es objeto. ')
    accion = 0
    if intencion == 1:
        accion = input('\nAtaque elegido es un numero del 0 al 3. ')
    elif intencion == 0:
        accion = input('\nObjeto Elegido debe ser el Nombre del objeto a usar. ')

    FinPartida = Juego().batalla(i, intencion, accion)
    EscribirEstats()
    i += 1