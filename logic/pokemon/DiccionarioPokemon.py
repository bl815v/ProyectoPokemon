from logic.pokemon.pokemones.Bulbasaur import Bulbasaur
from logic.pokemon.pokemones.Butterfree import Butterfree
from logic.pokemon.pokemones.Charmander import Charmander
from logic.pokemon.pokemones.Heracross import Heracross
from logic.pokemon.pokemones.Leafeon import Leafeon
from logic.pokemon.pokemones.Luxray import Luxray
from logic.pokemon.pokemones.Monferno import Monferno
from logic.pokemon.pokemones.Onix import Onix
from logic.pokemon.pokemones.Pikachu import Pikachu
from logic.pokemon.pokemones.Squirtle import Squirtle
from logic.pokemon.pokemones.Sudowoodo import Sudowoodo
from logic.pokemon.pokemones.Vaporeon import Vaporeon

class DiccionarioPokemon():
    """Clase que se encarga de crear el diccionario con la informacion de todos los pokemones.

    Attributes:
        Bulbasaur1: Lista con los valores del pokemon bulbasaur.
        Butterfree1: Lista con los valores del pokemon butterfree.
        Charmander1: Lista con los valores del pokemon charmander.
        Heracross1: Lista con los valores del pokemon heracross.
        Leafeon1: Lista con los valores del pokemon leafeon.
        Luxray1: Lista con los valores del pokemon luxray.
        Monferno1: Lista con los valores del pokemon monferno.
        Onix1: Lista con los valores del pokemon onix.
        Pikachu1: Lista con los valores del pokemon pikachu.
        Squirtle1: Lista con los valores del pokemon squirtle.
        Sudowoodo1: Lista con los valores del pokemon sudowoodo.
        Vaporeon1: Lista con los valores del pokemon vaporeon.
        Pokemones: Diccionario con los nombres de los pokemones y las listas de cada pokemon.
        pokA: Establece la posicion en la que está el pokemon elegido.
        pokB: Establece los datos elegidos del diccionario.
        pokC: Establece el tipo de dato a elegir de la lista del pokemon elegido.
        ListaPokemones: Lista con la informacion del pokemon elegido.
        ListaPropiedades: Lista con las estadisticas del pokemon elegido.

       """

    def __init__(self):
        """Inicializa DiccionarioPokemon con los argumentos.
  
       """
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
        """Devuelve la estadistica solicitada o la lista completa del pokemon seleccionado.
        Args:
            NombrePokemon: String con el nombre del pokemon elegido.
            TipoEstadistica: Sting con el nombre de la estadistica requerida.

        Returns:
            Pokemones: Diccionario con los nombres de los pokemones y las listas de cada pokemon.
            ListaPokemones: Lista con la informacion del pokemon elegido.
            ListaPropiedades: Lista con las estadisticas del pokemon elegido.
        """
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
        """Devuelve un numero que será la posicion en la que está ubicado el pokemon requerido en el diccionario.
        Args:
            pokemon: String con el nombre del pokemon elegido.

        Returns:
            Int con valores del 0 al 12
        """
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
        """Devuelve un numero que será la posicion en la que esta ubicado la estadistica en la lista del pokemon elegido.
        Args:
            Estat: String con la estadistica elegida.
        Returns:
            Int con valores del 0 al 7
        """
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
       """Devuelve una lista con todos los pokemones.

        Returns:
            Pokemones: Diccionario con los nombres de los pokemones y las listas de cada pokemon.
        """
       return list(self.Pokemones.values())