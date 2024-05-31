CREATE DATABASE batallasPokemon;
USE batallasPokemon;

CREATE TABLE usuarios (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,    
    correo VARCHAR(50) NOT NULL,
    usuario VARCHAR(50) NOT NULL,
    contrasena VARCHAR(50) NOT NULL,
    partidasganadas INT DEFAULT 0,
    partidasperdidas INT DEFAULT 0
);  