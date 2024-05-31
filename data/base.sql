CREATE TABLE usuarios (
    correo VARCHAR(50) NOT NULL,
    usuario VARCHAR(50) NOT NULL,
    contraseña VARCHAR(50) NOT NULL,
    partidasganadas INT DEFAULT 0,
    partidasperdidas INT DEFAULT 0
);  