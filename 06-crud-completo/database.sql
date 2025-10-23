CREATE DATABASE cinema_final;
USE cinema_final;

CREATE TABLE filmes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(60),
    genero VARCHAR(30),
    ano INT,
    avaliacao DECIMAL(3,1)
);

INSERT INTO filmes (titulo, genero, ano, avaliacao) VALUES
('Interestelar', 'Ficção Científica', 2014, 9.0),
('O Rei Leão', 'Animação', 1994, 8.5),
('Jurassic Park', 'Aventura', 1993, 8.1);
