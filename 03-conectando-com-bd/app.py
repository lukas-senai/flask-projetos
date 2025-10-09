from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Bem-vindo à Loja Flask!</h1><p><a href='/produtos'>Ver produtos</a></p>"

@app.route("/produtos")
def listar_produtos():
    conexao = mysql.connector.connect(host='localhost', user='root', password='', database='cherry_store')
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return render_template("produtos.html", produtos=produtos)

if __name__ == "__main__":
    app.run(debug=True)
