from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    print("Retornar o index.html e enviar um título para a página")
    pass

@app.route("/produtos")
def listar_produtos():
    print("Criar uma lista de produtos (nome, preço, estoque)")
    print("Retornar produtos.html passando essa lista")
    pass

if __name__ == "__main__":
    app.run(debug=True)
