from Logic.Movimientos.Movimiento import Movimiento

class ListaMovimiento:

    def crearMovimientos(self):

        self.Hidropulso = Movimiento("Hidropulso", 60, 100, 2, "Agua")
        self.Torbellino = Movimiento("Torbellino", 35, 85, 3, "Agua")
        self.Placaje = Movimiento("Placaje", 40, 100, 4, "Normal")
        self.Surf = Movimiento("Surf", 90, 100, 1, "Agua")
        self.Hidrobomba = Movimiento("Hidrobomba", 110, 80, 1, "Agua")
        self.RayoAurora = Movimiento("RayoAurora", 65, 100, 3, "Agua")
        self.Meteoros = Movimiento("Meteoros", 60, 60, 4, "Normal")
        self.Arañazo = Movimiento("Arañazo", 40, 100, 4, "Fuego")
        self.Ascuas = Movimiento("Ascuas", 40, 100, 3, "Fuego")
        self.Lanzallamas = Movimiento("Lanzallamas", 90, 100, 2, "Fuego")
        self.ColmilloFuego = Movimiento("ColmilloFuego", 65, 95, 3, "Fuego")
        self.Ultrapuño = Movimiento("Ultrapuño", 40, 100, 4, "Fuego")
        self.EnviteIgneo = Movimiento("EnviteIgneo", 120, 100, 1, "Fuego")
        self.RuedaIuego = Movimiento("RuedaFuego", 60, 100, 3, "Fuego")
        self.HojaAfilada = Movimiento("HojaAfilada", 55, 95, 3, "Planta")
        self.Latigazo = Movimiento("Latigazo", 120, 85, 2, "Planta")
        self.RayoSolar = Movimiento("RayoSolar", 120, 100, 1, "Planta")
        self.LlueveHojas = Movimiento("LlueveHojas", 130, 90, 1, "Planta")
        self.EnergiBola = Movimiento("EnergiBola", 90, 100, 2, "Planta")
        self.BombaGermen = Movimiento("BombaGermen", 80, 100, 3, "Planta")
        self.Cornada = Movimiento("Cornada", 65, 100, 3, "Bicho")
        self.PinMisil = Movimiento("PinMisil", 80, 95, 1, "Bicho")
        self.Picadura = Movimiento("Picadura", 60, 100, 3, "Bicho")
        self.Zumbido = Movimiento("Zumbido", 90, 100, 1, "Bicho")
        self.Psicorrayo = Movimiento("Psicorrayo", 65, 100, 3, "Bicho")
        self.TajoAereo = Movimiento("TajoAereo", 75, 95, 3, "Bicho")
        self.Impactrueno = Movimiento("Impactrueno", 40, 100, 4, "Electrico")
        self.Rayo = Movimiento("Rayo", 90, 100, 2, "Electrico")
        self.Trueno = Movimiento("Trueno", 110, 7, 1, "Electrico")
        self.Chispa = Movimiento("Chispa", 65, 100, 3, "Electrico")
        self.VoltioCruel = Movimiento("VoltioCruel", 90, 100, 3, "Electrico")
        self.Avalancha = Movimiento("Avalancha", 75, 90, 3, "Roca")
        self.TumbaRocas = Movimiento("TumbaRocas", 60, 95, 3, "Roca")
        self.Mazazo = Movimiento("Mazazo", 120, 100, 1, "Roca")
        self.Pedrada = Movimiento("Pedrada", 50, 90, 4, "Roca")
        self.Terratemblor = Movimiento("Terratemblor", 60, 100, 3, "Roca")
        self.ColaFerrea = Movimiento("ColaFerrea", 100, 75, 2, "Roca")

        self.ListaMovimientos = {
                                "Hidropulso": self.Hidropulso.getPropiedades(),
                                "Torbellino": self.Torbellino.getPropiedades(),
                                "Placaje": self.Placaje.getPropiedades(),
                                "Surf": self.Surf.getPropiedades(),
                                "Hidrobomba": self.Hidrobomba.getPropiedades(),
                                "RayoAurora": self.RayoAurora.getPropiedades(),
                                "Meteoros": self.Meteoros.getPropiedades(),
                                "Arañazo": self.Arañazo.getPropiedades(),
                                "Ascuas": self.Ascuas.getPropiedades(),
                                "Lanzallamas": self.Lanzallamas.getPropiedades(),
                                "ColmilloFuego": self.ColmilloFuego.getPropiedades(),
                                "Ultrapuño": self.Ultrapuño.getPropiedades(),
                                "EnviteIgneo": self.EnviteIgneo.getPropiedades(),
                                "RuedaFuego": self.RuedaIuego.getPropiedades(),
                                "HojaAfilada": self.HojaAfilada.getPropiedades(),
                                "Latigazo": self.Latigazo.getPropiedades(),
                                "RayoSolar": self.RayoSolar.getPropiedades(),
                                "LlueveHojas": self.LlueveHojas.getPropiedades(),
                                "EnergiBola": self.EnergiBola.getPropiedades(),
                                "BombaGermen": self.BombaGermen.getPropiedades(),
                                "Cornada": self.Cornada.getPropiedades(),
                                "PinMisil": self.PinMisil.getPropiedades(),
                                "Picadura": self.Picadura.getPropiedades(),
                                "Zumbido": self.Zumbido.getPropiedades(),
                                "Psicorrayo": self.Psicorrayo.getPropiedades(),
                                "TajoAereo": self.TajoAereo.getPropiedades(),
                                "Impactrueno": self.Impactrueno.getPropiedades(),
                                "Rayo": self.Rayo.getPropiedades(),
                                "Trueno": self.Trueno.getPropiedades(),
                                "Chispa": self.Chispa.getPropiedades(),
                                "VoltioCruel": self.VoltioCruel.getPropiedades(),
                                "Avalancha": self.Avalancha.getPropiedades(),
                                "TumbaRocas": self.TumbaRocas.getPropiedades(),
                                "Mazazo": self.Mazazo.getPropiedades(),
                                "Pedrada": self.Pedrada.getPropiedades(),
                                "Terratemblor": self.Terratemblor.getPropiedades(),
                                "ColaFerrea": self.ColaFerrea.getPropiedades()
                                }
        
        return list(self.ListaMovimientos.values())

    def getmovimiento(self):
        ListaMovimiento.crearMovimientos(self)
        return(self.hidropulso.getNombre())


