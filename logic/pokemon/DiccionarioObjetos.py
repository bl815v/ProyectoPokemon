from logic.mochila.BolaLodo import BolaLodo
from logic.mochila.Eter import Eter
from logic.mochila.Hierro import Hierro
from logic.mochila.HuesoRaro import HuesoRaro
from logic.mochila.Pocion import Pocion
from logic.mochila.Proteina import Proteina

class DiccionarioObjetos():
    """Clase que se encarga de crear el diccionario con todos lo objetos.

    Attributes:
        BolaLodo1: Lista con los valores del objeto BolaLodo.
        Eter1: Lista con los valores del objeto Eter.
        Hierro1: Lista con los valores del objeto Hierro.
        HuesoRaro1: Lista con los valores del objeto HuesoRaro.
        Pocion1: Lista con los valores del objeto Pocion.
        Proteina1: Lista con los valores del objeto Proteina.
        Objetos: Diccionario con los nombres de los objetos y las listas de cada objetos.
        objA: Establece la posicion en la que está el objeto elegido.
        objB: Establece los datos elegidos del diccionario.
        objC: Establece el tipo de dato a elegir de la lista del objeto elegido.
        ListaObjetos: Lista con la informacion del objeto pelegido.
        ListaPropiedades: Lista con las estadisticas del objeto elegido.

       """

    def DiccionarioDeObjetos(self, NombreObjeto, TipoEstadistica):
        """Devuelve la estadistica solicitada o la lista completa del objeto seleccionado.
        Args:
            NombreObjeto: String con el nombre del objeto elegido.
            TipoEstadistica: Sting con el nombre de la estadistica requerida.

        Returns:
            Objetos: Diccionario con los nombres de los objetos y las listas de cada objeto.
            ListaObjetos: Lista con la informacion del objeto elegido.
            ListaPropiedades: Lista con las estadisticas del objeto elegido.
        """
        self.objA = DiccionarioObjetos.IdentificarObjeto(NombreObjeto)
        self.objB = 1
        self.objC = DiccionarioObjetos.IdentificarEstadistica(TipoEstadistica)

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
        
        #Esta parte devuelve los datos que se requirieron especificamente en el constructor
        self.ListaObjetos = list(self.Objetos.items())
        self.ListaPropiedades = list(self.ListaObjetos[self.objA][self.objB])
        
        if self.objA>=0 and self.objA<=5:
            if self.objB==0:
                return self.ListaObjetos[self.objA][self.objB]
            elif self.objB==1:
                if self.objC>=0 and self.objC <= 5:
                    return self.ListaPropiedades[self.objC]
                else:
                    return self.ListaPropiedades
        else:
            return list(self.Objetos.values())
    

    def IdentificarObjeto(objeto):
        """Devuelve un numero que será la posicion en la que está ubicado el objeto requerido en el diccionario.
        Args:
            objeto: String con el nombre del objeto elegido.

        Returns:
            Int con valores del 0 al 6
        """
        if objeto == "BolaLodo":
            return 0
        elif objeto == "Eter":
            return 1
        elif objeto == "Hierro":
            return 2
        elif objeto == "HuesoRaro":
            return 3
        elif objeto == "Pocion":
            return 4
        elif objeto == "Proteina":
            return 5
        else:
            return 6
    
    def IdentificarEstadistica(Estat):
        """Devuelve un numero que será la posicion en la que esta ubicado la estadistica en la lista del objeto elegido.
        Args:
            Estat: String con la estadistica elegida.

        Returns:
            Int con valores del 0 al 6
        """
        if Estat == "Nombre":
            return 0
        elif Estat == "PS":
            return 1
        elif Estat == "PP":
            return 2
        elif Estat == "Ataque":
            return 3
        elif Estat == "Defensa":
            return 4
        elif Estat == "Cantidad":
            return 5
        elif Estat == "Todo":
            return 6