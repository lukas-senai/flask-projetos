CREATE DATABASE academia_flask;
USE academia_flask;

CREATE TABLE alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(60),
    idade INT,
    plano VARCHAR(20)
);

INSERT INTO alunos (nome, idade, plano) VALUES
('Lucas Almeida', 25, 'Mensal'),
('Carla Souza', 32, 'Trimestral'),
('Rafaela Torres', 20, 'Semestral'),
('Pedro Henrique', 27, 'Mensal'),
('Mariana Lopes', 22, 'Anual');

CREATE TABLE treinos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(60),
    nivel VARCHAR(20),
    duracao INT
);

INSERT INTO treinos (nome, nivel, duracao) VALUES
('Treino Iniciante', 'Fácil', 30),
('Treino Intermediário', 'Médio', 45),
('Treino Avançado', 'Difícil', 60),
('Treino Cardio', 'Médio', 40),
('Treino de Força', 'Difícil', 50);
