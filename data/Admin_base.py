class Admin_base:

    """Clase que se encarga de guardar o consultar datos de la base de datos.
     
    Args:
        db: Objeto que representa la conexiona a la base de datos.

    Attributes:
        db: Objeto que representa la conexiona a la base de datos.
    
       """
    def __init__(self, db):
        """Inicializa Admin_base con la conexion a la base de datos.
        Args:
            db: Objeto que representa la conexiona a la base de datos.
        """
        self.db = db
    
    def guardarUsuario(self, usuario, contrasena, correo):
        """Guarda un usuario en la base de datos.
        Args:
            usuario (String): Nombre del usuario.
            contrasena (String): Contraseña del usuario.
            correo (String): Correo del usuario.
        """
        cursor = self.db.connection.cursor()
        cursor.execute("INSERT INTO usuarios (correo, usuario, contraseña) VALUES ( %s, %s, %s)",
                    (correo, usuario, contrasena))
        self.db.connection.commit()
        cursor.close()    

    def validarUsuario(self, user, contrasena): 
        """Valida el usuario y la contraseña para realizar el login.
        Args:
            user (String): Nombre del usuario.
            contrasena (String): Contraseña del usuario.

        Returns:
            True or False: bool True si el usuario coincide con la contraseña, False si no coinciden.
        """
        cur = self.db.connection.cursor()
        cur.execute("SELECT * FROM usuarios WHERE usuario = %s AND contraseña = %s", (user, contrasena))
        usuario = cur.fetchone()
        cur.close()
        return True if usuario else False

    def getUsuarios(self):
        """Obtiene los usuarios registrados en la base de datos.
        
        Returns:
            Clientes: Es una lista con los usuarios registrados.
        """
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT * FROM usuarios")
        clientes = cursor.fetchall()
        cursor.close()
        return clientes
    
    def getUsuarioEspecifico(self, user): 
        """Obtiene un usuario en especifico con su nombre de usuario.
        Args:
            user (String): Nombre del usuario.

        Returns:
            Clientes: Usuario obtenido con el nombre de usuario.
        """
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario = %s", (user))
        clientes = cursor.fetchall()
        cursor.close()
        return clientes
    
    def aumentarPartidasGanadas(self, user):
        """Aumenta las partidas ganadas en la base de datos si el usuario gano.
        Args:
            user (String): Nombre del usuario.
        """
        cursor = self.db.connection.cursor()
        cursor.execute("UPDATE usuarios SET partidasganadas = partidasganadas + 1 WHERE user = %s;",(user))
        self.db.connection.commit()
        cursor.close()  
        
    def aumentarPartidasPerdidas(self, user):
        """Aumenta las partidas perdidas en la base de datos si el usuario gano.
        Args:
            user (String): Nombre del usuario.
        """
        cursor = self.db.connection.cursor()
        cursor.execute("UPDATE usuarios SET partidasperdidas = partidasperdidas + 1 WHERE user = %s;",(user))
        self.db.connection.commit()
        cursor.close()  
