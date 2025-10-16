from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

conexao = mysql.connector.connect(host='localhost', port='3406', user='root', password='', database='cinema_1610')
cursor = conexao.cursor(dictionary=True)

@app.route("/")
def index():
    cursor.execute("SELECT * FROM filmes")
    filmes = cursor.fetchall()
    return render_template("index.html", filmes=filmes)

@app.route("/novo")
def novo_filme():
    return render_template("novo-filme.html")

@app.route("/salvar-filme", methods=["POST"])
def salvar_filme():
    titulo = request.form["titulo"]
    genero = request.form["genero"]
    ano = request.form["ano"]
    avaliacao = request.form["avaliacao"]

    sql = "INSERT INTO filmes (titulo, genero, ano, avaliacao) VALUES (%s, %s, %s, %s)"
    valores = (titulo, genero, ano, avaliacao)
    cursor.execute(sql, valores)
    conexao.commit()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
