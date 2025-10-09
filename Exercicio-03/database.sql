CREATE DATABASE cinema_flask;
USE cinema_flask;

-- Tabela de filmes
CREATE TABLE filmes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(60),
    genero VARCHAR(30),
    ano INT,
    avaliacao DECIMAL(3,1)
);

INSERT INTO filmes (titulo, genero, ano, avaliacao) VALUES
('Inception', 'Ficção Científica', 2010, 8.8),
('O Rei Leão', 'Animação', 1994, 9.0),
('Interestelar', 'Ficção Científica', 2014, 8.6),
('Titanic', 'Romance', 1997, 7.9),
('Vingadores: Ultimato', 'Ação', 2019, 8.4),
('O Poderoso Chefão', 'Drama', 1972, 9.2),
('Coringa', 'Drama', 2019, 8.5),
('Avatar', 'Aventura', 2009, 7.8),
('Toy Story', 'Animação', 1995, 8.3),
('Homem-Aranha: Sem Volta para Casa', 'Ação', 2021, 8.2);

-- Tabela de salas
CREATE TABLE salas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50),
    capacidade INT,
    localizacao VARCHAR(50)
);

INSERT INTO salas (nome, capacidade, localizacao) VALUES
('Sala 1', 100, 'Térreo'),
('Sala 2', 120, 'Térreo'),
('Sala 3', 80, '1º Andar'),
('Sala 4', 60, '1º Andar'),
('Sala VIP', 40, '2º Andar');
