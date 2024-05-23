from Movimiento import Movimiento

class ListaMovimiento:

    def crearMovimientos(self):

        self.hidropulso = Movimiento("Hidropulso", 60, 100, 2, "Agua")
        self.torbellino = Movimiento("Torbellino", 35, 85, 3, "Agua")
        self.placaje = Movimiento("Torbellino", 40, 100, 4, "Normal")
        self.surf = Movimiento("surf", 90, 100, 1, "Agua")

        hidrobomba = Movimiento("hidrobomba", 110, 80, 1, "Agua")
        rayo_aurora = Movimiento("Rayo aurora", 65, 100, 3, "Agua")
        meteoros = Movimiento("meteoros", 60, 60, 4, "Normal")

        arañazo = Movimiento("Arañazo", 40, 100, 4, "Fuego")
        ascuas = Movimiento("Ascuas", 40, 100, 3, "Fuego")
        lanzallamas = Movimiento("Lanzallamas", 90, 100, 2, "Fuego")
        colmillo_fuego = Movimiento("Colmillo fuego", 65, 95, 3, "Fuego")

        ultrapuño = Movimiento("Ultrapuño", 40, 100, 4, "Fuego")
        envite_igneo = Movimiento("Envite igneo", 120, 100, 1, "Fuego")
        rueda_fuego = Movimiento("Rueda fuego", 60, 100, 3, "Fuego")

        hoja_afilada = Movimiento("Hoja afilada", 55, 95, 3, "Planta")
        latigazo = Movimiento("latigazo", 120, 85, 2, "Planta")
        rayo_solar = Movimiento("Rayo solar", 120, 100, 1, "Planta")

        llueve_hojas = Movimiento("Llueve hojas", 130, 90, 1, "Planta")
        energibola = Movimiento("Energibola", 90, 100, 2, "Planta")
        bomba_germen = Movimiento("Bomba germen", 80, 100, 3, "Planta")

        cornada = Movimiento("Cornada", 65, 100, 3, "Bicho")
        pin_misil = Movimiento("Pin_misil", 80, 95, 1, "Bicho")
        picadura = Movimiento("Picadura", 60, 100, 3, "Bicho")

        zumbido = Movimiento("Zumbido", 90, 100, 1, "Bicho")
        psicorrayo = Movimiento("Psicorrayo", 65, 100, 3, "Bicho")
        tajo_aereo = Movimiento("Tajo aereo", 75, 95, 3, "Bicho")

        impactrueno = Movimiento("Impactrueno", 40, 100, 4, "Electrico")
        rayo = Movimiento("Rayo", 90, 100, 2, "Electrico")
        trueno = Movimiento("Trueno", 110, 7, 1, "Electrico")
        chispa = Movimiento("Chispa", 65, 100, 3, "Electrico")

        voltio_cruel = Movimiento("Voltio cruel", 90, 100, 3, "Electrico")

        avalancha = Movimiento("Avalancha", 75, 90, 3, "Roca")
        tumba_rocas = Movimiento("Tumba rocas", 60, 95, 3, "Roca")
        mazazo = Movimiento("Mazazo", 120, 100, 1, "Roca")
        pedrada = Movimiento("Pedrada", 50, 90, 4, "Roca")

        terratemblor = Movimiento("Terratemblor", 60, 100, 3, "Roca")
        cola_ferrea = Movimiento("Cola ferrea", 100, 75, 2, "Roca")

    def getmovimiento(self):
        return(self.hidropulso.getNombre())


