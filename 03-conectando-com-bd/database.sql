CREATE DATABASE cherry_store;
USE cherry_store;

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50),
    preco DECIMAL(10,2),
    categoria VARCHAR(30)
);

INSERT INTO produtos (nome, preco, categoria) VALUES
('Mouse Gamer', 120.00, 'Periféricos'),
('Teclado Mecânico', 250.00, 'Periféricos'),
('Headset', 180.00, 'Periféricos'),
('Monitor 24"', 890.00, 'Periféricos'),
('Webcam Full HD', 210.00, 'Periféricos'),

('Placa de Vídeo GTX 1660', 1650.00, 'Hardware'),
('Processador Ryzen 5 5600G', 950.00, 'Hardware'),
('Memória RAM 16GB DDR4', 320.00, 'Hardware'),
('SSD 480GB', 290.00, 'Hardware'),
('Fonte 600W', 370.00, 'Hardware'),

('Cadeira Gamer', 1150.00, 'Acessórios'),
('Mousepad Grande', 80.00, 'Acessórios'),
('Caixa de Som Bluetooth', 150.00, 'Acessórios'),
('Hub USB 3.0', 90.00, 'Acessórios'),
('Suporte para Notebook', 130.00, 'Acessórios');
