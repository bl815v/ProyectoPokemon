from Logic.Movimientos.Movimiento import Movimiento

class ListaMovimiento:

    def crearMovimientos(self, movA):
            #37 movimientos(0-36)
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
                                "Hidropulso": self.Hidropulso.getPropiedades(), #0
                                "Torbellino": self.Torbellino.getPropiedades(), #1
                                "Placaje": self.Placaje.getPropiedades(), #2
                                "Surf": self.Surf.getPropiedades(), #3
                                "Hidrobomba": self.Hidrobomba.getPropiedades(), #4
                                "RayoAurora": self.RayoAurora.getPropiedades(), #5
                                "Meteoros": self.Meteoros.getPropiedades(), #6
                                "Arañazo": self.Arañazo.getPropiedades(), #7
                                "Ascuas": self.Ascuas.getPropiedades(), #8
                                "Lanzallamas": self.Lanzallamas.getPropiedades(), #9
                                "ColmilloFuego": self.ColmilloFuego.getPropiedades(), #10
                                "Ultrapuño": self.Ultrapuño.getPropiedades(), #11
                                "EnviteIgneo": self.EnviteIgneo.getPropiedades(), #12
                                "RuedaFuego": self.RuedaIuego.getPropiedades(), #13
                                "HojaAfilada": self.HojaAfilada.getPropiedades(), #14
                                "Latigazo": self.Latigazo.getPropiedades(), #15
                                "RayoSolar": self.RayoSolar.getPropiedades(), #16
                                "LlueveHojas": self.LlueveHojas.getPropiedades(), #17
                                "EnergiBola": self.EnergiBola.getPropiedades(), #18
                                "BombaGermen": self.BombaGermen.getPropiedades(), #19
                                "Cornada": self.Cornada.getPropiedades(), #20
                                "PinMisil": self.PinMisil.getPropiedades(), #21
                                "Picadura": self.Picadura.getPropiedades(), #22
                                "Zumbido": self.Zumbido.getPropiedades(), #23
                                "Psicorrayo": self.Psicorrayo.getPropiedades(), #24
                                "TajoAereo": self.TajoAereo.getPropiedades(), #25
                                "Impactrueno": self.Impactrueno.getPropiedades(), #26
                                "Rayo": self.Rayo.getPropiedades(), #27
                                "Trueno": self.Trueno.getPropiedades(), #28
                                "Chispa": self.Chispa.getPropiedades(), #29
                                "VoltioCruel": self.VoltioCruel.getPropiedades(), #30
                                "Avalancha": self.Avalancha.getPropiedades(), #31
                                "TumbaRocas": self.TumbaRocas.getPropiedades(), #32
                                "Mazazo": self.Mazazo.getPropiedades(), #33
                                "Pedrada": self.Pedrada.getPropiedades(), #34
                                "Terratemblor": self.Terratemblor.getPropiedades(), #35
                                "ColaFerrea": self.ColaFerrea.getPropiedades() #36
                                }
        
        self.ListaPropiedades = list(self.ListaMovimientos.values())
        return self.ListaPropiedades[movA]

    def EstadisticasMovimientos(self, pokemon, movimiento, estadistica):
        self.movimiento = ListaMovimiento.IdentifMovsPokemon(self, pokemon)
        self.estA = ListaMovimiento.IdentificarEstadistica(estadistica)

        if self.estA>=0 and self.estA <= 4:
            return self.movimiento[movimiento-1][self.estA]
        else:
            return self.movimiento[movimiento-1]
        #ListaMovimiento.crearMovimientos(self)
        #return(self.hidropulso.getNombre())

    def IdentifMovsPokemon(self, pokemon):
        if pokemon == "Bulbasaur":
            return (ListaMovimiento.crearMovimientos(self, 2), ListaMovimiento.crearMovimientos(self, 14), 
                    ListaMovimiento.crearMovimientos(self, 15), ListaMovimiento.crearMovimientos(self, 16))
        elif pokemon == "Butterfree":
            return (ListaMovimiento.crearMovimientos(self, 22), ListaMovimiento.crearMovimientos(self, 23), 
                    ListaMovimiento.crearMovimientos(self, 24), ListaMovimiento.crearMovimientos(self, 25))
        elif pokemon == "Charmander":
            return (ListaMovimiento.crearMovimientos(self, 7), ListaMovimiento.crearMovimientos(self, 8), 
                    ListaMovimiento.crearMovimientos(self, 9), ListaMovimiento.crearMovimientos(self, 10))
        elif pokemon == "Heracross":
            return (ListaMovimiento.crearMovimientos(self, 2), ListaMovimiento.crearMovimientos(self, 20), 
                    ListaMovimiento.crearMovimientos(self, 21), ListaMovimiento.crearMovimientos(self, 22))
        elif pokemon == "Leafeon":
            return (ListaMovimiento.crearMovimientos(self, 7), ListaMovimiento.crearMovimientos(self, 17), 
                    ListaMovimiento.crearMovimientos(self, 18), ListaMovimiento.crearMovimientos(self, 19))
        elif pokemon == "Luxray":
            return (ListaMovimiento.crearMovimientos(self, 2), ListaMovimiento.crearMovimientos(self, 30), 
                    ListaMovimiento.crearMovimientos(self, 26), ListaMovimiento.crearMovimientos(self, 28))
        elif pokemon == "Monferno":
            return (ListaMovimiento.crearMovimientos(self, 11), ListaMovimiento.crearMovimientos(self, 12), 
                    ListaMovimiento.crearMovimientos(self, 13), ListaMovimiento.crearMovimientos(self, 9))
        elif pokemon == "Onix":
            return (ListaMovimiento.crearMovimientos(self, 2), ListaMovimiento.crearMovimientos(self, 35), 
                    ListaMovimiento.crearMovimientos(self, 36), ListaMovimiento.crearMovimientos(self, 31))
        elif pokemon == "Pikachu":
            return (ListaMovimiento.crearMovimientos(self, 26), ListaMovimiento.crearMovimientos(self, 27), 
                    ListaMovimiento.crearMovimientos(self, 28), ListaMovimiento.crearMovimientos(self, 29))
        elif pokemon == "Squirtle":
            return (ListaMovimiento.crearMovimientos(self, 0), ListaMovimiento.crearMovimientos(self, 1), 
                    ListaMovimiento.crearMovimientos(self, 2), ListaMovimiento.crearMovimientos(self, 3))
        elif pokemon == "Sudowoodo":
            return (ListaMovimiento.crearMovimientos(self, 31), ListaMovimiento.crearMovimientos(self, 32), 
                    ListaMovimiento.crearMovimientos(self, 33), ListaMovimiento.crearMovimientos(self, 34))
        elif pokemon == "Vaporeon":
            return (ListaMovimiento.crearMovimientos(self, 0), ListaMovimiento.crearMovimientos(self, 4), 
                    ListaMovimiento.crearMovimientos(self, 5), ListaMovimiento.crearMovimientos(self, 6))
        else:
            return 0

    def IdentificarEstadistica(Estat):
        if Estat == "Nombre":
            return 0
        elif Estat == "Tipo":
            return 1
        elif Estat == "Potencia":
            return 2
        elif Estat == "Precision":
            return 3
        elif Estat == "PP":
            return 4
        elif Estat == "Todo":
            return 5