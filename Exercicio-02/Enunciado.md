## Tarefas para implementar:

1. **Página inicial (rota `/`)**

   * Fazer a rota retornar o `index.html`.
   * Exibir o título recebido do Python (ex.: “Catálogo de Filmes Flask”).
   * Adicionar links para as outras páginas do site: `/filmes` e `/sobre`.

2. **Lista de filmes (rota `/filmes`)**

   * O arquivo `app.py` já envia uma lista de filmes com `título`, `ano` e `gênero`.
   * Criar o `filmes.html` exibindo os filmes em uma **tabela** com `for`.
   * Cada linha deve mostrar as informações de um filme.
   * Adicionar um link “Voltar” para retornar à página inicial.

3. **Página sobre (rota `/sobre`)**

   * Criar o `sobre.html` com um pequeno texto explicando o propósito do site.
   * Adicionar o seu nome.
   * Inserir um link para voltar à página inicial.

4. **Desafio extra (opcional, mas legal):**

   * Destacar os filmes lançados **após 2020**, usando uma condição `if` no HTML.
   * Exemplo:

     ```html
     {% if filme.ano > 2020 %}
         <td>{{ filme.ano }} (filme recente)</td>
     {% else %}
         <td>{{ filme.ano }}</td>
     {% endif %}
     ```
