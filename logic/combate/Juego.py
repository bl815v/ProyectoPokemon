from logic.pokemon.DiccionarioPokemon import DiccionarioPokemon
from logic.pokemon.PokemonBase import PokemonBase
from logic.pokemon.DiccionarioObjetos import DiccionarioObjetos 
from logic.movimientos.ListaMovimiento import ListaMovimiento 

import random

class Juego():
    
    """Clase que se encarga de realizar la logica del combate pokemon.
     
    Attributes:
        diccionario(objeto): Objeto que representa el diccionario de objetos que se puden usar.
        objetosUser(List): Representa la lista de objetos disponibles del usuario.
        objetosPc(List): Representa la lista de objetos disponibles del pc.
        pokemon_pc(List): Lista con los atributos del pokemon del pc.
        pokemon_user(List): Lista con los atributos del pokemon del usuario.
        vidaPokemonPc(Int): Define la vida del pokemon del pc.
        ataquePokemonPc(Int): Define el ataque del pokemon del pc.
        defensaPokemonPc(Int): Define la defensa del pokemon del pc.
        tipoPokemonPc(String): Define el tipo del pokemon del pc.
        debilidadadPokemonPc(List): Define las debilidades del pokemon del pc.
        resistenciaPokemonPc(List): Define las fortalezas del pokemon del pc.
        movimientosPokemonPc(List): Define los movimientos pokemon del pc.
        vidaPokemonUser(Int): Define la vida del pokemon del usuario.
        ataquePokemonUser(Int): Define el ataque del pokemon del usuario.
        defensaPokemonUser(Int): Define la defensa del pokemon del usuario.
        tipoPokemonUser(String): Define el tipo del pokemon del usuario.
        debilidadadPokemonUser(List): Define las debilidades del pokemon del usuario.
        resistenciaPokemonUser(List): Define las fortalezas del pokemon del usuario.
        movimientosPokemonUser(List): Define los movimientos pokemon del usuario.
        combrobacionesDanopc()(Int): Si el pokemon del pc es resistente sera igual a 2, si es debil sera igual a 0.5.
        combrobacionesDanousuario()(Int): Si el pokemon del usuario es resistente sera igual a 2, si es debil sera igual a 0.5.
       """
    def __init__(self):
        """Inicializa Juego para iniciar la batalla.
        Args:
            diccionario(objeto): Objeto que representa el diccionario de objetos que se puden usar.
            objetosUser(List): Representa la lista de objetos disponibles del usuario.
            objetosPc(List): Representa la lista de objetos disponibles del pc.
        """
        self.diccionario = DiccionarioObjetos()
        self.objetosUser = [self.diccionario.DiccionarioDeObjetos("BolaLodo","Todo"),
                            self.diccionario.DiccionarioDeObjetos("Eter","Todo"),
                            self.diccionario.DiccionarioDeObjetos("Hierro","Todo"),
                            self.diccionario.DiccionarioDeObjetos("HuesoRaro","Todo"),
                            self.diccionario.DiccionarioDeObjetos("Pocion","Todo"),
                            self.diccionario.DiccionarioDeObjetos("Proteina","Todo")] 
        self.objetosPc = [self.diccionario.DiccionarioDeObjetos("BolaLodo","Todo"),
                            self.diccionario.DiccionarioDeObjetos("Eter","Todo"),
                            self.diccionario.DiccionarioDeObjetos("Hierro","Todo"),
                            self.diccionario.DiccionarioDeObjetos("HuesoRaro","Todo"),
                            self.diccionario.DiccionarioDeObjetos("Pocion","Todo"),
                            self.diccionario.DiccionarioDeObjetos("Proteina","Todo")] 
        

    def elegirPokemones(self, numero1, numero2):
        """Elige los pokemones que estaran en el combate y define los atributos de cada pokemon.
        Args:
            numero1 (Int): numero aleatorio para definir el pokemon del pc.
            numero2 (Int): numero aleatorio para definir el pokemon del usuario.

        """
        diccionario = DiccionarioPokemon.getPokemones(self)

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
        """Revisa si el pokemon del pc tiene debilidada o resistencia respecto al pokemon del usuario.        
        """
        self.comprobaciondanoPc = 1
        for elemento in self._pokemon_user[5]: #si el tipo de pokemon esta en las debilidades el daño se multiplicara por dos
            if elemento == self._pokemon_pc[1]:
                self.comprobaciondanoPc = 2

        for elemento in self._pokemon_user[6]: #si el tipo de pokemon esta en las fortalezas el daño se reduce a la mitad
            if elemento == self._pokemon_pc[1]:
                self.comprobaciondanoPc = 0.5 

    def debilidadResistenciaUser(self):
        """Revisa si el pokemon del usuario tiene debilidada o resistencia respecto al pokemon del pc.        
        """
        self.comprobaciondanoUser = 1
        for elemento in self._pokemon_pc[5]: 
            if elemento == self._pokemon_user[1]:
                self.comprobaciondanoUser = 2

        for elemento in self._pokemon_pc[6]:
            if elemento == self._pokemon_user[1]:
                self.comprobaciondanoUser = 0.5

    def AumentarPpMovimiento(self, quien, aumento):
        """Aumenta el pp del pokemon elegido.
        Args:
            quien (String): User si quiere aumentar el pp del usuario o Pc si quiere aumentar el pp del Pc.
        """
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

    def UsarObjetoUsuario(self,objeto): 
        """Realiza el comportamiento de un objeto si un usuario usa un objeto.
        Args:
            objeto (String): nombre del objeto que usa el usuario.

        Returns:
            "El objeto elegido no esta disponible, elige un objeto diferente" si el objeto esta agotado
            el pokemon " ha usado " objeto si el objeto esta disponible y ha sio usado
        """
        objetoElegido = self.diccionario.DiccionarioDeObjetos(objeto,"Todo")
        while(objetoElegido[5] == 0): 
            return("El objeto elegido no esta disponible, elige un objeto diferente") 
        
        posicion = DiccionarioObjetos.IdentificarObjeto(objetoElegido[0])     
        self.objeto = self.objetosUser[posicion]
        self.objetosUser[posicion][5] -= 1
        
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
        """Realiza el comportamiento de un objeto si el pc usa un objeto.

        Returns:
            el pokemon ha usado objeto cuando el pokemon pc haya usado el objeto
        """ 
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
    
    def realizarAtaqueUsuario(self,ataque):
        """Realiza la logica cuando el pokemon de un usuario realiza un ataque.
        Args:
            Ataque (Int): numero del movimiento realizado, de 0 a 3 dependiendo cual de los 4 movimientos elige el usuario.

        Returns:
            El ataque elegido no tiene puntos disponibles, elige un ataque diferente" si el ataque esta sin puntos disponibles
            self._pokemon_user[0] + "ha fallado el ataque" si el pokemon realiza el ataque pero lo falla
            self._pokemon_user[0] + "ha realizado el ataque" + self.movimientosPokemonUser[ataque][0] si el pokemon acierta el ataque
        """
        ataqueElegido = self.movimientosPokemonUser[ataque]
        while(ataqueElegido[4] == 0):
            return("El ataque elegido no tiene puntos disponibles, elige un ataque diferente") 

        pokemonUser = PokemonBase(0,0,0,0,0,0,0)
        Juego.debilidadResistenciaUser(self)  
        dano = pokemonUser.CalcDano(ataqueElegido[2],self.getPokemon_user()[3],self.getPokemon_pc()[4]) * self.comprobaciondanoUser

        aleatorio_precision = random.random()
        if aleatorio_precision <= ataqueElegido[3]:  
            vida = self.getVidaPokemon_pc()
            self.setVidaPokemon_pc(vida - dano) 
            self.movimientosPokemonUser[ataque][4] - 1
            return(self._pokemon_user[0] + "ha realizado el ataque" + self.movimientosPokemonUser[ataque][0])
            
        else:
            return(self._pokemon_user[0] + "ha fallado el ataque")
        
        
    def turnoUsuario(self,intencion,accion): 
        """Simula el turno del usuario dependiendo si el usuario quiere realizar un ataque o usar un objeto.
        Args:
            Intencion (Int): 0 si el usuario quiere elegir un objeto, 1 si el usuario quiere hacer un ataque.
        """
        if(intencion == 0):
            self.setObjetoelegido(accion) 
            self.UsarObjetoUsuario(self.objetoElegido) 
        else:
            self.realizarAtaqueUsuario(accion) 
        
        
    def realizarAtaquePc(self):
        """Realiza la logica cuando el pokemon del Pc realiza un ataque.

        Returns:
            self._pokemon_pc[0] + "ha fallado el ataque" si el pokemon realiza el ataque pero lo falla
            self._pokemon_pc[0] + "ha realizado el ataque" + self.movimientosPokemonPc[ataque][0] si el pokemon acierta el ataque
        """
        ataque = random.randint(0, 3)
        ataqueElegido = self.movimientosPokemonPc[ataque]  
        while(ataqueElegido[4] == 0):   #Para combrobar el PP del ataque es con la posicion 4
            ataque = random.randint(0, 3)
            ataqueElegido = self.movimientosPokemonPc[ataque]  
            #si el ataque no esta disponible no pude avanzar la ejecucion del programa


        pokemonPc = PokemonBase(0,0,0,0,0,0,0)
        Juego.debilidadResistenciaPc(self)  #se comprueba si es debil o resistente
        dano = pokemonPc.CalcDano(ataqueElegido[2],self.getPokemon_pc()[3],self.getPokemon_user()[4]) * self.comprobaciondanoPc
        #calcula el daño con los parametros de potencia del movimiento, ataque del pokemon y defensa del pokemon contrario

        aleatorio_precision = random.random() # crea un numero de 0 a 1
        if aleatorio_precision <= ataqueElegido[3]: #se simula el porcentaje de precicion del movimiento 
            vida = self.getVidaPokemon_user()
            self.setVidaPokemon_user(vida - dano) #se actualiza la vida del pokemon enemigo restando el daño calculado
            self.movimientosPokemonPc[ataque][4] - 1 # le resta 1 al pp del movimiento
            return(self._pokemon_pc[0] + "ha realizado el ataque" + self.movimientosPokemonPc[ataque][0])
            
        else:
            return(self._pokemon_user[0] + "ha fallado el ataque")
        
        
    def turnoPc(self):
        """Realiza la logica del turno del pc, simulando una probabilidad de usar un objeto o realizar un ataque.
        """
        if(self.getVidaPokemon_pc() <= self.vidaTotalPc - 20):
            aleatorio = random.random()
            if(aleatorio<=0.8):
                self.UsarObjetoPc()
            else:
                self.realizarAtaquePc()
        else:
            self.realizarAtaquePc()
                    
        
    def batalla(self, i, intencion, accion): 
        """Simula toda la batalla del pokemon.
        Args:
            i (Int): El turno en el que se encuentre la batalla.
            i (intencion): Si es el turno del usuario sera 0 si quiere usar objeto 0 1 si quiere realizar ataque.

        Returns:
            "has perdido" si la vida del pokemon del usuario llega a 0. 
            "has ganado" si la vida del pokemon del pc llega a 0.    
        """
        if i % 2 == 0:
            self.turnoPc()
        else:
            self.turnoUsuario(intencion, accion)
        
        if self.getVidaPokemon_user() <= 0:
            print("\nHas perdido")
            return 1
        elif self.getVidaPokemon_pc() <= 0:
            print("\nHas ganado")
            return 1
                
        return 0


    def getPokemon_pc(self):
        """Obtiene los atributos del pokemon del pc.
        
        Returns:
            atributos del pokemon del pc.
        """
        return self._pokemon_pc
        
    def getPokemon_user(self):
        """Obtiene los atributos del pokemon del usuario.
        
        Returns:
            atributos del pokemon del usuario.
        """
        return self._pokemon_user
    
    def getVidaPokemon_user(self):
        """Obtiene la vida del pokemon del usuario.
        
        Returns:
            vida del pokemon del usuario.
        """
        return self.vidaPokemonUser
    
    def setVidaPokemon_user(self, vida):
        """Define la vida del pokemon del usuario.
        Args:
            vida (Int): vida del pokemon del usuario.
        """
        self.vidaPokemonUser = vida

    def getAtaquePokemon_user(self):
        """Obtiene el ataque del pokemon del usuario.
        
        Returns:
            ataque del pokemon del usuario.
        """
        return self.ataquePokemonUser
    
    def setAtaquePokemon_user(self, ataque):
        """Define el ataque del pokemon del usuario.
        Args:
            ataque (Int): ataque del pokemon del usuario.
        """
        self.ataquePokemonUser = ataque

    def getDefensaPokemon_user(self):
        """Obtiene la defensa del pokemon del usuario.
        
        Returns:
            defensa del pokemon del usuario.
        """
        return self.defensaPokemonUser
    
    def setDefensaPokemon_user(self, defensa):
        """Define la defensa del pokemon del usuario.
        Args:
            defensa (Int): defensa del pokemon del usuario.
        """
        self.defensaPokemonUser = defensa

    def getTipoPokemon_user(self):
        """Obtiene el tipo del pokemon del usuario.
        
        Returns:
            tipo del pokemon del usuario.
        """
        return self.tipoPokemonUser
    
    def setTipoPokemon_user(self, tipo):
        """Define el tipo del pokemon del usuario.
        Args:
            tipo (Strin): tipo del pokemon del usuario.
        """
        self.tipoPokemonUser = tipo

    def getDebilidadPokemon_user(self):
        """Obtiene la debilidad del pokemon del usuario.
        
        Returns:
            debilidad del pokemon del usuario.
        """
        return self.debilidadPokemonUser
    
    def setDebilidadPokemon_user(self, debilidad):
        """Define las debilidades del pokemon del usuario.
        Args:
            debilidad (list): debilidades del pokemon del usuario.
        """
        self.debilidadPokemonUser = debilidad

    def getResistenciaPokemon_user(self):
        """Obtiene la resistencia del pokemon del usuario.
        
        Returns:
            resistencia del pokemon del usuario.
        """
        return self.resistenciaPokemonUser
    
    def setResistenciaPokemon_user(self, resistencia):
        """Define la resistencia del pokemon del usuario.
        Args:
            resistencia (Int): resistencia del pokemon del usuario.
        """
        self.resistenciaPokemonUser = resistencia

    def getMovimientosPokemon_user(self):
        """Obtiene los movimientos del pokemon del usuario.
        
        Returns:
            movimientos del pokemon del usuario.
        """
        return self.movimientosPokemonUser
    
    def setMovimientosPokemon_user(self, numeroDeAtaque, cambio):
        """Define los movimientos del pokemon del usuario.
        Args:
            numeroDeAtaque (Int): posicion del ataque.
            cambio (List): atributos del ataque.
        """
        self.movimientosPokemonUser[numeroDeAtaque][4] = cambio

    def getVidaPokemon_pc(self):
        """Obtiene la vida del pokemon del Pc.
        
        Returns:
            vida del pokemon del Pc.
        """
        return self.vidaPokemonPc
    
    def setVidaPokemon_pc(self, vida):
        """Define la vida del pokemon del Pc.
        Args:
            vida (Int): vida del pokemon del Pc.
        """
        self.vidaPokemonPc = vida

    def getAtaquePokemon_pc(self):
        """Obtiene el ataque del pokemon del pc.
        
        Returns:
            ataque del pokemon del pc.
        """
        return self.ataquePokemonPc
    
    def setAtaquepokemon_pc(self, ataque):
        """Define el ataque del pokemon del pc.
        Args:
            ataque (Int): ataque del pokemon del pc.
        """
        self.ataquePokemonPc = ataque

    def getDefensaPokemon_pc(self):
        """Obtiene la defensa del pokemon del pc.
        
        Returns:
            defensa del pokemon del pc.
        """
        return self.defensaPokemonPc
    
    def setDefensaPokemon_pc(self, defensa):
        """Define la defensa del pokemon del pc.
        Args:
            defensa (Int): defensa del pokemon del pc.
        """
        self.defensaPokemonPc = defensa
    
    def getTipoPokemon_pc(self):
        """Obtiene el tipo del pokemon del pc.
        
        Returns:
            tipo del pokemon del pc.
        """
        return self.tipoPokemonPc
    
    def setTipoPokemon_pc(self, tipo):
        """Define el tipo del pokemon del pc.
        Args:
            tipo (String): tipo del pokemon del pc.
        """
        self.tipoPokemonPc = tipo

    def getDebilidadPokemon_pc(self):
        """Obtiene la debilidad del pokemon del pc.
        
        Returns:
            debilidad del pokemon del pc.
        """
        return self.debilidadPokemonPc
    
    def setDebilidadPokemon_pc(self, debilidad):
        """Define el ataque del pokemon del pc.
        Args:
            ataque (Int): ataque del pokemon del pc.
        """
        self.debilidadPokemonPc = debilidad

    def getResistenciaPokemon_pc(self):
        """Obtiene la resistencia del pokemon del pc.
        
        Returns:
            resistencia del pokemon del pc.
        """
        return self.resistenciaPokemonPc
    
    def setResistenciaPokemon_pc(self, resistencia):
        """Define la resistencia del pokemon del pc.
        Args:
            resistencia (Int): resistencia del pokemon del pc.
        """
        self.resistenciaPokemonPc = resistencia

    def getMovimientosPokemon_pc(self):
        """Obtiene los movimientos del pokemon del pc.
        
        Returns:
            movimientos del pokemon del pc.
        """
        return self.movimientosPokemonPc
    
    def setMovimientosPokemon_pc(self, numeroDeAtaque, cambio):
        """Define los movimientos del pokemon del pc.
        Args:
            numeroDeAtaque (Int): posicion del ataque.
            cambio (List): atributos del ataque.
        """
        [numeroDeAtaque][4] = cambio
