from Logic.Pokemon.Pokemones.Bulbasaur import Bulbasaur
from Logic.Pokemon.Pokemones.Butterfree import Butterfree
from Logic.Pokemon.Pokemones.Charmander import Charmander
from Logic.Pokemon.Pokemones.Heracross import Heracross
from Logic.Pokemon.Pokemones.Leafeon import Leafeon
from Logic.Pokemon.Pokemones.Luxray import Luxray
from Logic.Pokemon.Pokemones.Monferno import Monferno
from Logic.Pokemon.Pokemones.Onix import Onix
from Logic.Pokemon.Pokemones.Pikachu import Pikachu
from Logic.Pokemon.Pokemones.Squirtle import Squirtle
from Logic.Pokemon.Pokemones.Sudowoodo import Sudowoodo
from Logic.Pokemon.Pokemones.Vaporeon import Vaporeon

class DiccionarioPokemon():

    def __init__(self):
        self.Bulbasaur1 = Bulbasaur(0,0,0,0,0,0,0)
        self.Butterfree1 = Butterfree(0,0,0,0,0,0,0)
        self.Charmander1 = Charmander(0,0,0,0,0,0,0)
        self.Heracross1 = Heracross(0,0,0,0,0,0,0)
        self.Leafeon1 = Leafeon(0,0,0,0,0,0,0)
        self.Luxray1 = Luxray(0,0,0,0,0,0,0)
        self.Monferno1 = Monferno(0,0,0,0,0,0,0)
        self.Onix1 = Onix(0,0,0,0,0,0,0)
        self.Pikachu1 = Pikachu(0,0,0,0,0,0,0)
        self.Squirtle1 = Squirtle(0,0,0,0,0,0,0)
        self.Sudowoodo1 = Sudowoodo(0,0,0,0,0,0,0)
        self.Vaporeon1 = Vaporeon(0,0,0,0,0,0,0)
        self.Pokemones = {
                        "Bulbasaur": self.Bulbasaur1.getPropiedades(),
                        "Butterfree": self.Butterfree1.getPropiedades(),
                        "Charmander": self.Charmander1.getPropiedades(),
                        "Heracross": self.Heracross1.getPropiedades(),
                        "Leafeon": self.Leafeon1.getPropiedades(),
                        "Luxray": self.Luxray1.getPropiedades(),
                        "Monferno": self.Monferno1.getPropiedades(),
                        "Onix": self.Onix1.getPropiedades(),
                        "Pikachu": self.Pikachu1.getPropiedades(),
                        "Squirtle": self.Squirtle1.getPropiedades(),
                        "Sudowoodo": self.Sudowoodo1.getPropiedades(),
                        "Vaporeon": self.Vaporeon1.getPropiedades()
                        }

    def DiccionarioDePokemon(self, NombrePokemon, TipoEstadistica):
        #12 pokemones
        self.Bulbasaur1 = Bulbasaur(0,0,0,0,0,0,0)
        self.Butterfree1 = Butterfree(0,0,0,0,0,0,0)
        self.Charmander1 = Charmander(0,0,0,0,0,0,0)
        self.Heracross1 = Heracross(0,0,0,0,0,0,0)
        self.Leafeon1 = Leafeon(0,0,0,0,0,0,0)
        self.Luxray1 = Luxray(0,0,0,0,0,0,0)
        self.Monferno1 = Monferno(0,0,0,0,0,0,0)
        self.Onix1 = Onix(0,0,0,0,0,0,0)
        self.Pikachu1 = Pikachu(0,0,0,0,0,0,0)
        self.Squirtle1 = Squirtle(0,0,0,0,0,0,0)
        self.Sudowoodo1 = Sudowoodo(0,0,0,0,0,0,0)
        self.Vaporeon1 = Vaporeon(0,0,0,0,0,0,0)
        self.Pokemones = {
                        "Bulbasaur": self.Bulbasaur1.getPropiedades(),
                        "Butterfree": self.Butterfree1.getPropiedades(),
                        "Charmander": self.Charmander1.getPropiedades(),
                        "Heracross": self.Heracross1.getPropiedades(),
                        "Leafeon": self.Leafeon1.getPropiedades(),
                        "Luxray": self.Luxray1.getPropiedades(),
                        "Monferno": self.Monferno1.getPropiedades(),
                        "Onix": self.Onix1.getPropiedades(),
                        "Pikachu": self.Pikachu1.getPropiedades(),
                        "Squirtle": self.Squirtle1.getPropiedades(),
                        "Sudowoodo": self.Sudowoodo1.getPropiedades(),
                        "Vaporeon": self.Vaporeon1.getPropiedades()
                        }
    
        self.pokA = DiccionarioPokemon.IdentificarPokemon(NombrePokemon)
        self.pokB = 1
        self.pokC = DiccionarioPokemon.IdentificarEstadistica(TipoEstadistica)
        
        #Esta parte devuelve los datos que se requirieron especificamente en el constructor
        self.ListaPokemones = list(self.Pokemones.items())
        self.ListaPropiedades = list(self.ListaPokemones[self.pokA][self.pokB])
        if self.pokA>=0 and self.pokA<=11:
            if self.pokB==0:
                return self.ListaPokemones[self.pokA][self.pokB]
            elif self.pokB==1:
                if self.pokC>=0 and self.pokC <= 6:
                    return self.ListaPropiedades[self.pokC]
                else:
                    return self.ListaPropiedades
        else:
            return list(self.Pokemones.values())

    def IdentificarPokemon(pokemon):
        if pokemon == "Bulbasaur":
            return 0
        elif pokemon == "Butterfree":
            return 1
        elif pokemon == "Charmander":
            return 2
        elif pokemon == "Heracross":
            return 3
        elif pokemon == "Leafeon":
            return 4
        elif pokemon == "Luxray":
            return 5
        elif pokemon == "Monferno":
            return 6
        elif pokemon == "Onix":
            return 7
        elif pokemon == "Pikachu":
            return 8
        elif pokemon == "Squirtle":
            return 9
        elif pokemon == "Sudowoodo":
            return 10
        elif pokemon == "Vaporeon":
            return 11
        else:
            return 12
    
    def IdentificarEstadistica(Estat):
        if Estat == "Nombre":
            return 0
        elif Estat == "Tipo":
            return 1
        elif Estat == "Vida":
            return 2
        elif Estat == "Ataque":
            return 3
        elif Estat == "Defensa":
            return 4
        elif Estat == "Debilidad":
            return 5
        elif Estat == "Resistencia":
            return 6
        elif Estat == "Todo":
            return 7

    def getPokemones(self):
       return list(self.Pokemones.values())