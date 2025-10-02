from flask import Flask, render_template

app = Flask(__name__)

# Página inicial
@app.route("/")
def home():
    return render_template("index.html")

# Página de alunos com dados fixos
@app.route("/alunos")
def mostrar_alunos():
    # Lista de dados fixa no Python
    alunos = [
        {"nome": "Ana", "idade": 20, "nota": 8.5},
        {"nome": "Carlos", "idade": 22, "nota": 7.0},
        {"nome": "Maria", "idade": 19, "nota": 9.2},
        {"nome": "João", "idade": 21, "nota": 6.8},
    ]
    # Envia a lista para o template
    return render_template("alunos.html", lista_alunos=alunos)

if __name__ == "__main__":
    app.run(debug=True)
