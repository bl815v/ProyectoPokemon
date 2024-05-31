class Movimiento:
    def __init__(self, nombre, potencia, precision, PP, tipo):
        self.nombre = nombre
        self.potencia = potencia
        self.precision = precision / 100
        self.PP = PP
        self.tipo = tipo

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getPotencia(self):
        return self.potencia

    def setPotencia(self, potencia):
        self.potencia = potencia

    def getPrecision(self):
        return self.precision

    def setPrecision(self, precision):
        self.precision = precision / 100

    def getPP(self):
        return self.PP

    def setPP(self, PP):
        self.PP = PP

    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo

    def getPropiedades(self):
        return (self.nombre, self.tipo, self.potencia, self.precision, self.PP)
    #Retorna una lista con las propiedades del movimiento
    

