from flask import Flask, render_template, request

app = Flask(__name__)

# Rota principal
@app.route("/")
def home():
    return render_template("index.html")

# Rota para mostrar o formulário
@app.route("/contato", methods=["GET"])
def mostrar_formulario():
    return render_template("contato.html")

# Rota para processar o formulário
@app.route("/enviar", methods=["POST"])
def processar_formulario():
    nome = request.form["nome"]
    email = request.form["email"]
    mensagem = request.form["mensagem"]
    return f"<h2>Obrigado, {nome}! Recebemos sua mensagem: {mensagem}</h2>"

if __name__ == "__main__":
    app.run(debug=True)
