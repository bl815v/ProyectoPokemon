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
        Juego.elegirPokemones(self)

    def elegirPokemones(self):
        numero1 = random.randint(0, 11) #genera un numero aleatorio del 0 al 11
        
        while(True):
            numero2 = random.randint(0, 11)
            if numero2 != numero1:  #genera un numero aleatorio y garantiza que no sea el mismo que el otro numero generado
                break
        
        diccionario = DiccionarioPokemon()
        self._pokemon_pc= diccionario.getPokemones()[numero1]
        self._pokemon_user=diccionario.getPokemones()[numero2]

        self.vidaPokemonPc = self._pokemon_pc[2]
        self.vidaTotalPc =  DiccionarioPokemon.DiccionarioDePokemon(self, self._pokemon_pc[0], 'Vida')#se define vida total para asegurar que los objetos no pongan mas vida que la maxima posible
        self.ataquePokemonPc = self._pokemon_pc[3]
        self.defensaPokemonPc = self._pokemon_pc[4]
        self.tipoPokemonPc = self._pokemon_pc[1]
        self.debilidadPokemonPc = self._pokemon_pc[5]
        self.resistenciaPokemonPc = self._pokemon_pc[6]
        self.movimientosPokemonPc = ListaMovimiento.IdentifMovsPokemon(self, self._pokemon_pc[0])

        self.vidaPokemonUser = self._pokemon_user[2]
        self.vidaTotalUser = DiccionarioPokemon.DiccionarioDePokemon(self, self._pokemon_user[0], 'Vida')
        self.ataquePokemonUser = self._pokemon_user[3]
        self.defensaPokemonUser = self._pokemon_user[4]
        self.tipoPokemonUser = self._pokemon_user[1]
        self.debilidadPokemonUser = self._pokemon_pc[5]
        self.resistenciaPokemonUser = self._pokemon_pc[6]
        self.movimientosPokemonUser = ListaMovimiento.IdentifMovsPokemon(self, self._pokemon_user[0])

        self.MovimientosPokemonPc = ListaMovimiento().IdentifMovsPokemon(self._pokemon_pc[0])
        self.MovimientosPokemonUser = ListaMovimiento().IdentifMovsPokemon(self._pokemon_user[0])



    def AumentarPpMovimiento(self, movimiento,aumento):
        movimiento[3] += aumento #aumenta el pp al movimiento


    def UsarObjetoUsuario(self,objeto):
        objetoElegido = self.diccionario.DiccionarioDeObjetos(objeto,"Todo")
        while(objetoElegido[5] == 0): #hace que no se pudean elegir objetos agotados
            return("El objeto elegido no tiene puntos disponibles, elige un objeto diferente") 
        posicion = self.diccionario.IdentificarObjeto(objetoElegido) #se le pasa el nombre del objeto que eligio el usuario    
        self.objeto = self.objetosUser[posicion]
        self.objetosUser[posicion][5] -= 1 #resta en uno a la cantidad del objeto elegido
        
        if(self.getVidaPokemon_user() + self.objeto[1] < self.vidaTotalUser): #hace que el pokemon no sobrepase la vida maxima con la que inicia
            self.setVidaPokemon_user(self.getVidaPokemon_user() + self.objeto[1])
        else:
             self.setVidaPokemon_user(self.vidaTotalUser)

        self.AumentarPpMovimiento(["ejemplo",40,50,3,"ag"],self.objeto[2]) #aumenta el pp de un movimiento
        self.setAtaquePokemon_user(self.getAtaquePokemon_user() + self.objeto[3]) #aumenta el ataque del pokemon
        self.setDefensaPokemon_user(self.getDefensaPokemon_user() + self.objeto[4]) #aumenta la defensa del pokemon
        return(self._pokemon_user[0] + "ha usado" + self.objeto[0])


    def UsarObjetoPc(self):       
        objetoAleatorio = random.randint(0,5)
        self.objeto = self.objetosPc[objetoAleatorio]
        self.objetosPc[objetoAleatorio][5] -= 1 
        if(self.getVidaPokemon_pc() + self.objeto[1] < self.vidaTotalPc): #hace que el pokemon no sobrepase la vida maxima con la que inicia
            self.setVidaPokemon_pc(self.getVidaPokemon_pc() + self.objeto[1])
        else:
             self.setVidaPokemon_pc(self.vidaTotalPc)

        self.AumentarPpMovimiento(["ejemplo",40,50,3,"ag"],self.objeto[2])
        self.setAtaquepokemon_pc(self.getAtaquePokemon_pc() + self.objeto[3])
        self.setDefensaPokemon_pc(self.getDefensaPokemon_pc() + self.objeto[4])
        return(self._pokemon_pc[0] + "ha usado" + self.objeto[0])


    def realizarAtaqueUsuario(self,ataque): #ataque es la posicion del movimiento elegido, si eligio el primer movimiento la posicion sera 0
        ataqueElegido = self.MovimientosPokemonUser[ataque]
        while(ataqueElegido[3] == 0):
            return("El ataque elegido no tiene puntos disponibles, elige un ataque diferente") 
            #si el ataque no esta disponible no pude avanzar la ejecucion del programa
             
        pokemonUser = Pokemon()
        daño = pokemonUser.CalcDaño(ataqueElegido[1],self.getPokemon_user()[3],self.getPokemon_pc()[4])
        #calcula el daño con los parametros de potencia del movimiento, ataque del pokemon y defensa del pokemon contrario

        aleatorio_precision = random.random() # crea un numero de 0 a 1

        if aleatorio_precision <= ataqueElegido[2]: #se simula el porcentaje de precicion del movimiento 
            vida = self.getVidaPokemon_pc()
            self.setVidaPokemon_pc(vida - daño) #se actualiza la vida del pokemon enemigo restando el daño calculado

            self.MovimientosPokemonUser[ataque][3] -= 1 # le resta 1 al pp del movimiento
            
        else:
            return(self._pokemon_user[0] + "ha fallado el ataque")
        
        
    def turnoUsuario(self,intencion,ataque): #intencion = 0 si quiere usar objeto y si quiere realizar ataque = 1 y ataque posicion del movimiento
        if(intencion == 0):
            self.UsarObjetoUsuario(self.objetoElegido)
        else:
            self.realizarAtaqueUsuario(ataque)
        
        
    def realizarAtaquePc(self):
        ataque = random.randint(0, 3)
        ataqueElegido = self.MovimientosPokemonPc[ataque]  
        while(ataqueElegido[3] == 0):
            ataque = random.randint(0, 3)
            ataqueElegido = self.MovimientosPokemonPc[ataque]  
            #si el ataque no esta disponible no pude avanzar la ejecucion del programa

          
        pokemonPc = Pokemon()
        daño = pokemonPc.CalcDaño(ataqueElegido[1],self.getPokemon_pc()[3],self.getPokemon_user()[4])
        #calcula el daño con los parametros de potencia del movimiento, ataque del pokemon y defensa del pokemon contrario

        aleatorio_precision = random.random() # crea un numero de 0 a 1

        if aleatorio_precision <= ataqueElegido[2]: #se simula el porcentaje de precicion del movimiento 
            vida = self.getVidaPokemon_user()
            self.setVidaPokemon_user(vida - daño) #se actualiza la vida del pokemon enemigo restando el daño calculado

            self.MovimientosPokemonPc[ataque][3] -= 1 # le resta 1 al pp del movimiento
            
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

                    
        
    
    def batalla(self, i, intencion, ataque): #se pasa en cada turno la intencion del usuario y el ataque elegido por el usuario
        if i % 2 == 0:
            self.turnoPc()
        else:
            self.turnoUsuario(intencion, ataque)
        if self.getVidaPokemon_user() <= 0:
            print("Has perdido")
        elif self.getVidaPokemon_pc() <= 0:
            print("Has ganado")


                


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

    def setAtaqueElegido(self, movimiento):
        self.AtaqueElegido = movimiento

    def getAtaqueElegido(self):
        return self.AtaqueElegido

    def getIntencion(self):
        return self.intencion
    
    def setIntencion(self,intencion):
        self.intencion = intencion

    def setObjetoElegido(self):
        return self.objetoElegido
    
    def getObjetoelegido(self,objeto):
        self.objetoElegido = objeto
            