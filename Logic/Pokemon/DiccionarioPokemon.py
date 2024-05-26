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

    def DiccionarioDePokemon(self):
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
                        "Squitle": self.Squirtle1.getPropiedades(),
                        "Sudowoodo": self.Sudowoodo1.getPropiedades(),
                        "Vaporeon": self.Vaporeon1.getPropiedades()
                        }
        
        return list(self.Pokemones.values())