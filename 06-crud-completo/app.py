from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Configuração do banco
config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'cinema_final'
}

# ------------------------------
# Página inicial
# ------------------------------
@app.route("/")
def home():
    return render_template("index.html")

# ------------------------------
# Listagem de filmes
# ------------------------------
@app.route("/filmes")
def listar_filmes():
    conexao = mysql.connector.connect(**config)
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM filmes ORDER BY titulo")
    filmes = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template("lista_filmes.html", filmes=filmes)

# ------------------------------
# Formulário de novo filme
# ------------------------------
@app.route("/novo", methods=["GET"])
def novo_filme():
    return render_template("novo_filme.html")

# ------------------------------
# Salvar novo filme (POST)
# ------------------------------
@app.route("/salvar", methods=["POST"])
def salvar_filme():
    titulo = request.form["titulo"]
    genero = request.form["genero"]
    ano = request.form["ano"]
    avaliacao = request.form["avaliacao"]

    conexao = mysql.connector.connect(**config)
    cursor = conexao.cursor()
    sql = "INSERT INTO filmes (titulo, genero, ano, avaliacao) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (titulo, genero, ano, avaliacao))
    conexao.commit()
    cursor.close()
    conexao.close()

    return redirect("/filmes")

# ------------------------------
# Editar filme
# ------------------------------
@app.route("/editar/<int:id>")
def editar_filme(id):
    conexao = mysql.connector.connect(**config)
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM filmes WHERE id = %s", (id,))
    filme = cursor.fetchone()
    cursor.close()
    conexao.close()
    return render_template("editar_filme.html", filme=filme)

# ------------------------------
# Atualizar filme (POST)
# ------------------------------
@app.route("/atualizar/<int:id>", methods=["POST"])
def atualizar_filme(id):
    titulo = request.form["titulo"]
    genero = request.form["genero"]
    ano = request.form["ano"]
    avaliacao = request.form["avaliacao"]

    conexao = mysql.connector.connect(**config)
    cursor = conexao.cursor()
    sql = "UPDATE filmes SET titulo=%s, genero=%s, ano=%s, avaliacao=%s WHERE id=%s"
    cursor.execute(sql, (titulo, genero, ano, avaliacao, id))
    conexao.commit()
    cursor.close()
    conexao.close()
    return redirect("/filmes")

# ------------------------------
# Excluir filme
# ------------------------------
@app.route("/excluir/<int:id>")
def excluir_filme(id):
    conexao = mysql.connector.connect(**config)
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM filmes WHERE id=%s", (id,))
    conexao.commit()
    cursor.close()
    conexao.close()
    return redirect("/filmes")

# ------------------------------
# Rodar o app
# ------------------------------
if __name__ == "__main__":
    app.run(debug=True)
