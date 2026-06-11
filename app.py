from flask import Flask, render_template, request, redirect, session
from model.produtos import Produtos

app = Flask(__name__)
app.secret_key = 'Vexx777@'

@app.route('/')
def vexx_home():
    produtos = Produtos.recuperar_produtos()
    return render_template("pagina_inicial.html", produtos = produtos)


@app.route('/catalogo/categoria')
def vexx_catalogo_categoria():
    return render_template("categoria_unica.html")

@app.route('/cadastro')
def vexx_cadastro():
    return render_template("cadastro.html")


@app.route('/login')
def vexx_login():
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True) 