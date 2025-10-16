CREATE DATABASE cinema_cadastro;
USE cinema_cadastro;

CREATE TABLE filmes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(60),
    genero VARCHAR(30),
    ano INT,
    avaliacao DECIMAL(3,1)
);
