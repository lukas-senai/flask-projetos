
1. **Catálogo de filmes** 🎬

   * Conectar Flask ao banco `cinema_flask`
   * Tabela: `filmes (id, titulo, genero, ano, avaliacao)`
   * Exibir os filmes em cards, com o gênero e avaliação.

2. **Agenda de contatos** 📇

   * Banco `agenda_flask`
   * Tabela: `contatos (id, nome, telefone, email, categoria)`
   * Exibir contatos por categoria (família, amigos, trabalho).

# **🎬 Catálogo de Filmes com Flask e MySQL**

Um grande cinema da sua região quer colocar em seu site uma página com a **lista de filmes disponíveis**.
Eles contrataram você para desenvolver um protótipo usando **Flask** conectado ao banco de dados **MySQL**.

Seu papel é criar o site e deixá-lo funcional, com os dados vindos do banco.

---

## ⚙️ **Banco de Dados**

```sql
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
('Vingadores: Ultimato', 'Ação', 2019, 8.4);

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
```

---

## **Tarefas para implementar**

1. **Página inicial (`index.html`)**

    * Mostrar o nome do cinema e uma breve descrição (ex.: “Confira nossa seleção de grandes filmes!”).
    * Adicionar um botão ou link para `/filmes` e um para `/salas`.
    * Aplicar CSS básico (fundo colorido leve, fonte centralizada ou como achar mais bonito).

2. **Página de filmes (`filmes.html`)**

    * Exibir cada filme em um card simples com:

        * Título
        * Gênero
        * Ano
        * Avaliação (ex.: ⭐ 8.8)
    * Adicionar um link “Voltar” para retornar à página inicial.

3. **Página de salas (`salas.html`)**

    * Exibir cada sala em um card simples ou em uma tabela com:

        * Nome
        * Capacidade
        * Localização
    * Adicionar um link “Voltar” para retornar à página inicial e um para ir à página de filmes.

4. **Extra (opcional)**

    * Na página de filmes, destacar filmes com Avaliação maior ou igual a 8.

    * Na página de salas, destacar salas com capacidade maior ou igual 100.
