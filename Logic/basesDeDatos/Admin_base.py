class Baseusuarios:

    def __init__(self, db):
        self.db = db

    def guardarUsuario(self, usuario, contraseña, nombre): #guarda la contraseña, usuario y nombre ne la base de datos
        cursor = self.db.connection.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, usuario, contraseña) VALUES ( %s, %s, %s)",
                    (nombre, usuario, contraseña))
        self.db.connection.commit()
        cursor.close()    

    def validarUsuario(self, user, contraseña): #valida si la contraseña y usuario coinciden pra hacer el login
        cur = self.db.connection.cursor()
        cur.execute("SELECT * FROM usuarios WHERE usuario = %s AND contraseña = %s", (user, contraseña))
        usuario = cur.fetchone()
        cur.close()
        return True if usuario else False

    def getUsuarios(self): #devuelve todos los usuarios registrados
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT * FROM usuarios")
        clientes = cursor.fetchall()
        cursor.close()
        return clientes
    
    def getUsuarioEspecifico(self, user): #devuelve los datos de un usuario en forma de lista si le pasamos el user
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario = %s", (user))
        clientes = cursor.fetchall()
        cursor.close()
        return clientes
    
    def aumentarPartidasGanadas(self, user):
        cursor = self.db.connection.cursor()
        cursor.execute("UPDATE usuarios SET partidasganadas = partidasganadas + 1 WHERE user = %s;",(user))
        self.db.connection.commit()
        cursor.close()  
        
    def aumentarPartidasPerdidas(self, user):
        cursor = self.db.connection.cursor()
        cursor.execute("UPDATE usuarios SET partidasperdidas = partidasperdidas + 1 WHERE user = %s;",(user))
        self.db.connection.commit()
        cursor.close()  

    def setUsuario(self,usuario):
        self.usuario = usuario
    
    def getUsuario(self):
        return self.usuario
    
    def setContraseña(self,contraseña):
        self.contraseña = contraseña
    
    def getContraseña(self):
        return self.contraseña