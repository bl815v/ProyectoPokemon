from Logic.Pokemon.DiccionarioPokemon import DiccionarioPokemon
from Logic.Pokemon.PokemonBase import Pokemon
from Logic.Pokemon.DiccionarioObjetos import DiccionarioObjetos 
from Logic.Movimientos.ListaMovimiento import ListaMovimiento 

import random

class Juego():
    
    def __init__(self):
        self.diccionario = DiccionarioObjetos()
        self.objetosUser = [self.diccionario.DiccionarioDeObjetos("BolaLodo","Todo"),
                            self.diccionario.DiccionarioDeObjetos("Eter","Todo"),
                            self.diccionario.DiccionarioDeObjetos("Hierro","Todo"),
                            self.diccionario.DiccionarioDeObjetos("HuesoRaro","Todo"),
                            self.diccionario.DiccionarioDeObjetos("Pocion","Todo"),
                            self.diccionario.DiccionarioDeObjetos("Proteina","Todo")] #se crean los objetos del usuario
        self.objetosPc = [self.diccionario.DiccionarioDeObjetos("BolaLodo","Todo"),
                            self.diccionario.DiccionarioDeObjetos("Eter","Todo"),
                            self.diccionario.DiccionarioDeObjetos("Hierro","Todo"),
                            self.diccionario.DiccionarioDeObjetos("HuesoRaro","Todo"),
                            self.diccionario.DiccionarioDeObjetos("Pocion","Todo"),
                            self.diccionario.DiccionarioDeObjetos("Proteina","Todo")] #se crean los objetos del pc
        

    def elegirPokemones(self):
        numero1 = random.randint(0, 11) #genera un numero aleatorio del 0 al 11
        
        numero2 = random.randint(0, 11)
        
        diccionario = DiccionarioPokemon.getPokemones()
        
        self._pokemon_pc = diccionario[numero1]
        self._pokemon_user = diccionario[numero2]

        self.vidaPokemonPc = self._pokemon_pc[2]
        self.vidaTotalPc =  DiccionarioPokemon.DiccionarioDePokemon(self, self._pokemon_pc[0], 'Vida')#se define vida total para asegurar que los objetos no pongan mas vida que la maxima posible
        self.ataquePokemonPc = self._pokemon_pc[3]
        self.defensaPokemonPc = self._pokemon_pc[4]
        self.tipoPokemonPc = self._pokemon_pc[1]
        self.debilidadPokemonPc = self._pokemon_pc[5]
        self.resistenciaPokemonPc = self._pokemon_pc[6]
        self.movimientosPokemonPc = ListaMovimiento.IdentifMovsPokemon(self, self._pokemon_pc[0])
        self.movimientosPPMaximosPc = (self.movimientosPokemonPc[0][4], self.movimientosPokemonPc[1][4],
                                        self.movimientosPokemonPc[2][4], self.movimientosPokemonPc[3][4])

        self.vidaPokemonUser = self._pokemon_user[2]
        self.vidaTotalUser = DiccionarioPokemon.DiccionarioDePokemon(self, self._pokemon_user[0], 'Vida')
        self.ataquePokemonUser = self._pokemon_user[3]
        self.defensaPokemonUser = self._pokemon_user[4]
        self.tipoPokemonUser = self._pokemon_user[1]
        self.debilidadPokemonUser = self._pokemon_user[5]
        self.resistenciaPokemonUser = self._pokemon_user[6]
        self.movimientosPokemonUser = ListaMovimiento.IdentifMovsPokemon(self, self._pokemon_user[0])
        self.movimientosPPMaximosUser = (self.movimientosPokemonUser[0][4], self.movimientosPokemonUser[1][4],
                                        self.movimientosPokemonUser[2][4], self.movimientosPokemonUser[3][4])

    def debilidadResistenciaPc(self):
        self.comprobaciondañoPc = 1
        for elemento in self._pokemon_user[5]: #si el tipo de pokemon esta en las debilidades el daño se multiplicara por dos
            if elemento == self._pokemon_pc[1]:
                self.comprobaciondañoPc = 2

        for elemento in self._pokemon_user[6]: #si el tipo de pokemon esta en las fortalezas el daño se reduce a la mitad
            if elemento == self._pokemon_pc[1]:
                self.comprobaciondañoPc = 0.5 

    def debilidadResistenciaUser(self):
        self.comprobaciondañoUser = 1
        for elemento in self._pokemon_pc[5]: 
            if elemento == self._pokemon_user[1]:
                self.comprobaciondañoUser = 2

        for elemento in self._pokemon_pc[6]:
            if elemento == self._pokemon_user[1]:
                self.comprobaciondañoUser = 0.5

    def AumentarPpMovimiento(self, quien, aumento):
        if quien == 'User':
            if ((self.movimientosPokemonUser[0][4] + aumento) <= self.movimientosPPMaximosUser[0]):    #aumenta el pp al movimiento del usuario
                self.movimientosPokemonUser[0][4] + aumento
            else:
                self.movimientosPokemonUser[0][4]

            if ((self.movimientosPokemonUser[1][4] + aumento) <= self.movimientosPPMaximosUser[1]):    #aumenta el pp al movimiento del usuario
                self.movimientosPokemonUser[1][4] + aumento
            else:
                self.movimientosPokemonUser[1][4]

            if ((self.movimientosPokemonUser[2][4] + aumento) <= self.movimientosPPMaximosUser[2]):    #aumenta el pp al movimiento del usuario
                self.movimientosPokemonUser[2][4] + aumento
            else:
                self.movimientosPokemonUser[2][4]

            if ((self.movimientosPokemonUser[3][4] + aumento) <= self.movimientosPPMaximosUser[3]):    #aumenta el pp al movimiento del usuario
                self.movimientosPokemonUser[3][4] + aumento
            else:
                self.movimientosPokemonUser[3][4]
        elif quien == 'Pc':
            if ((self.movimientosPokemonPc[0][4] + aumento) <= self.movimientosPPMaximosPc[0]):    #aumenta el pp al movimiento del usuario
                self.movimientosPokemonPc[0][4] + aumento
            else:
                self.movimientosPokemonPc[0][4]

            if ((self.movimientosPokemonPc[1][4] + aumento) <= self.movimientosPPMaximosPc[1]):    #aumenta el pp al movimiento del usuario
                self.movimientosPokemonPc[1][4] + aumento
            else:
                self.movimientosPokemonPc[1][4]
                
            if ((self.movimientosPokemonPc[2][4] + aumento) <= self.movimientosPPMaximosPc[2]):    #aumenta el pp al movimiento del usuario
                self.movimientosPokemonPc[2][4] + aumento
            else:
                self.movimientosPokemonPc[2][4]

            if ((self.movimientosPokemonPc[3][4] + aumento) <= self.movimientosPPMaximosPc[3]):    #aumenta el pp al movimiento del usuario
                self.movimientosPokemonPc[3][4] + aumento
            else:
                self.movimientosPokemonPc[3][4]

    def UsarObjetoUsuario(self,objeto): #objeto es el nombre string del objeto escogido
        objetoElegido = self.diccionario.DiccionarioDeObjetos(objeto,"Todo")
        while(objetoElegido[5] == 0): #hace que no se pudean elegir objetos agotados
            return("El objeto elegido no esta disponible, elige un objeto diferente") 
        
        posicion = DiccionarioObjetos.IdentificarObjeto(objetoElegido[0]) #se le pasa el nombre del objeto que eligio el usuario    
        self.objeto = self.objetosUser[posicion]
        self.objetosUser[posicion][5] -= 1 #resta en uno a la cantidad del objeto elegido
        
        if(self.getVidaPokemon_user() + self.objeto[1] < self.vidaTotalUser): #hace que el pokemon no sobrepase la vida maxima con la que inicia
            self.setVidaPokemon_user(self.getVidaPokemon_user() + self.objeto[1])
        else:
             self.setVidaPokemon_user(self.vidaTotalUser)

        self.AumentarPpMovimiento('User', self.objeto[2]) #aumenta el pp de un movimiento

        if(self.objeto[3] > 0): 
            self.setAtaquePokemon_user(self.getAtaquePokemon_user() + self.objeto[3]) #aumenta el ataque del pokemon
        else:
            self.setAtaquepokemon_pc(self.getAtaquePokemon_pc() + self.objeto[3]) #si es negativo resta el ataque del enemigo
        if(self.objeto[4] > 0):
            self.setDefensaPokemon_user(self.getDefensaPokemon_user() + self.objeto[4]) #aumenta la defensa del pokemon
        else:
            self.setDefensaPokemon_pc(self.getDefensaPokemon_pc() + self.objeto[4])
        return(self._pokemon_user[0] + " ha usado " + self.objeto[0])
    
    def UsarObjetoPc(self):  
        movimiento =  random.randint(0,3) #elige un movimiento aleatorio para aumentarle el pp
        objetoAleatorio = random.randint(0,5)
        self.objeto = self.objetosPc[objetoAleatorio]
        self.objetosPc[objetoAleatorio][5] -= 1 
        if(self.getVidaPokemon_pc() + self.objeto[1] < self.vidaTotalPc): #hace que el pokemon no sobrepase la vida maxima con la que inicia
            self.setVidaPokemon_pc(self.getVidaPokemon_pc() + self.objeto[1])
        else:
             self.setVidaPokemon_pc(self.vidaTotalPc)

        self.AumentarPpMovimiento('Pc', self.objeto[2])

        if(self.objeto[3] > 0):
            self.setAtaquepokemon_pc(self.getAtaquePokemon_pc() + self.objeto[3])
        else:
            self.setAtaquePokemon_user(self.getAtaquePokemon_user() + self.objeto[3])
        if(self.objeto[4] > 0):
            self.setDefensaPokemon_pc(self.getDefensaPokemon_pc() + self.objeto[4])
        else:
            self.setDefensaPokemon_user(self.getDefensaPokemon_user() + self.objeto[4])
        return(self._pokemon_pc[0] + " ha usado " + self.objeto[0])
    
    def realizarAtaqueUsuario(self,ataque): #ataque es la posicion del movimiento elegido, si eligio el primer movimiento la posicion sera 0
        ataqueElegido = self.movimientosPokemonUser[ataque]
        while(ataqueElegido[4] == 0):
            return("El ataque elegido no tiene puntos disponibles, elige un ataque diferente") 
            #si el ataque no esta disponible no pude avanzar la ejecucion del programa

        pokemonUser = Pokemon(0,0,0,0,0,0,0)
        Juego.debilidadResistenciaUser(self)  #se comprueba si es debil o resistente
        daño = pokemonUser.CalcDaño(ataqueElegido[2],self.getPokemon_user()[3],self.getPokemon_pc()[4]) * self.comprobaciondañoUser
        #calcula el daño con los parametros de potencia del movimiento, ataque del pokemon y defensa del pokemon contrario

        aleatorio_precision = random.random() # crea un numero de 0 a 1
        if aleatorio_precision <= ataqueElegido[3]: #se simula el porcentaje de precicion del movimiento 
            vida = self.getVidaPokemon_pc()
            self.setVidaPokemon_pc(vida - daño) #se actualiza la vida del pokemon enemigo restando el daño calculado
            self.movimientosPokemonUser[ataque][4] - 1 # le resta 1 al pp del movimiento
            
        else:
            return(self._pokemon_user[0] + "ha fallado el ataque")
        
        
    def turnoUsuario(self,intencion,accion): #intencion = 0 si quiere usar objeto y si quiere realizar ataque = 1 y ataque posicion del movimiento
        if(intencion == 0):
            self.setObjetoelegido(accion) #ObjetoElegido debe ser un string con el Nombre del objeto
            self.UsarObjetoUsuario(self.objetoElegido) #movimiento debe ser un numero de 0 al 3 / 
        else:
            self.realizarAtaqueUsuario(accion) #Ataque elegido es un numero del 0 al 3, los movimientos
        
        
    def realizarAtaquePc(self):
        ataque = random.randint(0, 3)
        ataqueElegido = self.movimientosPokemonPc[ataque]  
        while(ataqueElegido[4] == 0):   #Para combrobar el PP del ataque es con la posicion 4
            ataque = random.randint(0, 3)
            ataqueElegido = self.movimientosPokemonPc[ataque]  
            #si el ataque no esta disponible no pude avanzar la ejecucion del programa


        pokemonPc = Pokemon(0,0,0,0,0,0,0)
        Juego.debilidadResistenciaPc(self)  #se comprueba si es debil o resistente
        daño = pokemonPc.CalcDaño(ataqueElegido[2],self.getPokemon_pc()[3],self.getPokemon_user()[4]) * self.comprobaciondañoPc
        #calcula el daño con los parametros de potencia del movimiento, ataque del pokemon y defensa del pokemon contrario

        aleatorio_precision = random.random() # crea un numero de 0 a 1
        if aleatorio_precision <= ataqueElegido[3]: #se simula el porcentaje de precicion del movimiento 
            vida = self.getVidaPokemon_user()
            self.setVidaPokemon_user(vida - daño) #se actualiza la vida del pokemon enemigo restando el daño calculado
            self.movimientosPokemonPc[ataque][4] - 1 # le resta 1 al pp del movimiento
            
        else:
            return(self._pokemon_user[0] + "ha fallado el ataque")
        
        
    def turnoPc(self):
        if(self.getVidaPokemon_pc() <= self.vidaTotalPc - 20):
            aleatorio = random.random()
            if(aleatorio<=0.8):
                self.UsarObjetoPc()
            else:
                self.realizarAtaquePc()
        else:
            self.realizarAtaquePc()
                    
        
    def batalla(self, i, intencion, accion): #se pasa en cada turno la intencion del usuario y el ataque elegido por el usuario
        if i % 2 == 0:
            self.turnoPc()
        else:
            self.turnoUsuario(intencion, accion) #intencion=0 si se usa objeto, =1 si es ataque / ataque es igual al movimiento escogido (0-3)
        
        if self.getVidaPokemon_user() <= 0:
            print("\nHas perdido")
            return 1
        elif self.getVidaPokemon_pc() <= 0:
            print("\nHas ganado")
            return 1
                
        return 0


    def getPokemon_pc(self):
        return self._pokemon_pc
        
    def getPokemon_user(self):
        return self._pokemon_user
    
    def getVidaPokemon_user(self):
        return self.vidaPokemonUser
    
    def setVidaPokemon_user(self, vida):
        self.vidaPokemonUser = vida

    def getAtaquePokemon_user(self):
        return self.ataquePokemonUser
    
    def setAtaquePokemon_user(self, ataque):
        self.ataquePokemonUser = ataque

    def getDefensaPokemon_user(self):
        return self.defensaPokemonUser
    
    def setDefensaPokemon_user(self, defensa):
        self.defensaPokemonUser = defensa

    def getTipoPokemon_user(self):
        return self.tipoPokemonUser
    
    def setTipoPokemon_user(self, tipo):
        self.tipoPokemonUser = tipo

    def getDebilidadPokemon_user(self):
        return self.debilidadPokemonUser
    
    def setDebilidadPokemon_user(self, debilidad):
        self.debilidadPokemonUser = debilidad

    def getResistenciaPokemon_user(self):
        return self.resistenciaPokemonUser
    
    def setResistenciaPokemon_user(self, resistencia):
        self.resistenciaPokemonUser = resistencia

    def getMovimientosPokemon_user(self):
        return self.movimientosPokemonUser
    
    def setMovimientosPokemon_user(self, numeroDeAtaque, cambio):
        self.movimientosPokemonUser[numeroDeAtaque][4] = cambio

    def getVidaPokemon_pc(self):
        return self.vidaPokemonPc
    
    def setVidaPokemon_pc(self, vida):
        self.vidaPokemonPc = vida

    def getAtaquePokemon_pc(self):
        return self.ataquePokemonPc
    
    def setAtaquepokemon_pc(self, ataque):
        self.ataquePokemonPc = ataque

    def getDefensaPokemon_pc(self):
        return self.defensaPokemonPc
    
    def setDefensaPokemon_pc(self, defensa):
        self.defensaPokemonPc = defensa
    
    def getTipoPokemon_pc(self):
        return self.tipoPokemonPc
    
    def setTipoPokemon_pc(self, tipo):
        self.tipoPokemonPc = tipo

    def getDebilidadPokemon_pc(self):
        return self.debilidadPokemonPc
    
    def setDebilidadPokemon_pc(self, debilidad):
        self.debilidadPokemonPc = debilidad

    def getResistenciaPokemon_pc(self):
        return self.resistenciaPokemonPc
    
    def setResistenciaPokemon_pc(self, resistencia):
        self.resistenciaPokemonPc = resistencia

    def getMovimientosPokemon_pc(self):
        return self.movimientosPokemonPc
    
    def setMovimientosPokemon_pc(self, numeroDeAtaque, cambio):
        self.movimientosPokemonPc[numeroDeAtaque][4] = cambio

    def setAtaqueElegido(self, movimiento):
        self.AtaqueElegido = movimiento

    def getAtaqueElegido(self):
        return self.AtaqueElegido
    
    def getIntencion(self):
        return self.intencion
    
    def setIntencion(self,intencion):
        self.intencion = intencion

    def getObjetoElegido(self):
        return self.objetoElegido
    
    def setObjetoelegido(self,objeto):
        self.objetoElegido = objeto