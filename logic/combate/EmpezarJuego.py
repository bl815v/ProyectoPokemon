from logic.combate.Juego import Juego

import random

num1 = random.randint(0, 11)
num2 = random.randint(0, 11)

Juego().elegirPokemones(num1, num2)
FinPartida = 0
j = 1
i = 1
while(FinPartida == 0):
    if j % 2 == 0:
        i = 0
    else: 
        i = 1
        
    intencion = input('\n1 es ataque, 0 es objeto. ')
    accion = 0
    if intencion == 1:
        accion = input('\nAtaque elegido es un numero del 0 al 3. ')
    elif intencion == 0:
        accion = input('\nObjeto Elegido debe ser el Nombre del objeto a usar. ')
    
    j += 1
    FinPartida = Juego().batalla(i, intencion, accion)
    #EscribirEstats()
    