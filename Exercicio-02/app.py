from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Página inicial do site
    return render_template("index.html", titulo="Catálogo de Filmes Flask")

@app.route("/filmes")
def filmes():
    # Lista de filmes. Pode adicionar mais se quiser.
    lista_filmes = [
        {"titulo": "Interstellar", "ano": 2014, "genero": "Ficção Científica"},
        {"titulo": "O Rei do Show", "ano": 2017, "genero": "Musical"},
        {"titulo": "A Origem", "ano": 2010, "genero": "Ação"},
        {"titulo": "Soul", "ano": 2020, "genero": "Animação"},
    ]
    return render_template("filmes.html", filmes=lista_filmes)

@app.route("/sobre")
def sobre():
    # Página de informações sobre o site
    return render_template("sobre.html")

if __name__ == "__main__":
    app.run(debug=True)
