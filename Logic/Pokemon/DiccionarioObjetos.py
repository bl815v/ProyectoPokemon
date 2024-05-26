from Logic.Mochila.BolaLodo import BolaLodo
from Logic.Mochila.Eter import Eter
from Logic.Mochila.Hierro import Hierro
from Logic.Mochila.HuesoRaro import HuesoRaro
from Logic.Mochila.Pocion import Pocion
from Logic.Mochila.Proteina import Proteina

class DiccionarioObjetos():

    def DiccionarioDeObjetos(self):
        self.BolaLodo1 = BolaLodo(0,0,0,0,0,0)
        self.Eter1 = Eter(0,0,0,0,0,0)
        self.Hierro1 = Hierro(0,0,0,0,0,0)
        self.HuesoRaro1 = HuesoRaro(0,0,0,0,0,0)
        self.Pocion1 = Pocion(0,0,0,0,0,0)
        self.Proteina1 = Proteina(0,0,0,0,0,0)

        self.Objetos = {
                        "BolaLodo": self.BolaLodo1.getPropiedades(),
                        "Eter": self.Eter1.getPropiedades(),
                        "Hierro": self.Hierro1.getPropiedades(),
                        "HuesoRaro": self.HuesoRaro1.getPropiedades(),
                        "Pocion": self.Pocion1.getPropiedades(),
                        "Proteina": self.Proteina1.getPropiedades()
                        }
        
        return list(self.Objetos.values())