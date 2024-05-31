class Usuario():
    """Clase que se encarga de la logica de usuario para la base de datos.
    Args:
            correo: correo del usuario.
            user: nombre de usuario.
            contraseña: contraseña del susuario.
    Attributes:
        correo: correo del usuario.
        user: nombre de usuario.
        contraseña: contraseña del susuario.
    
       """
    def __init__(self, correo, user, contraseña):
        """Inicializa la clase usuario.
        Args:
            correo: correo del usuario.
            user: nombre de usuario.
            contraseña: contraseña del susuario.
        """
        self.correo = correo
        self.usuario = user
        self.contraseña = contraseña

    def setCorreo(self,correo):
        """Define el correo del usuario.
        Args:
            correo (String): correo del usuario.
        """
        self.correo = correo

    def getCorreo(self):
        """Obtiene el correo del usuario.
        
        Returns:
            correo del usuario.
        """
        return self.correo
    
    def setUsuario(self,user):
        """Define el nombre de usuario.
        Args:
            user (String): nombre de usuario.
        """
        self.usuario = user

    def getUsuario(self):
        """Obtiene el nombre del usuario.
        
        Returns:
            nombre del usuario.
        """
        return self.usuario
    
    def setContraseña(self,contraseña):
        """Define la contraseña del usuario.
        Args:
            contraseña (String): contraseña del usuario.
        """
        self.contraseña = contraseña

    def getContraseña(self):
        """Obtiene la contraseña del usuario.
        
        Returns:
            contraseña del usuario.
        """
        return self.contraseña