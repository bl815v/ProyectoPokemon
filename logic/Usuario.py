class Usuario():
    def __init__(self, nombre, user, contraseña):
        self.nombre = nombre
        self.usuario = user
        self.contraseña = contraseña

    def setNombre(self,nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre
    
    def setUsuario(self,user):
        self.usuario = user

    def getUsuario(self):
        return self.usuario
    
    def setContraseña(self,contraseña):
        self.contraseña = contraseña

    def getNombre(self):
        return self.contraseña