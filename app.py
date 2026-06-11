from flask import Flask, render_template, request, redirect, session
from model.produtos import Produtos
from model.categoria import Categoria

app = Flask(__name__)
app.secret_key = 'Vexx777@'

@app.route('/')
def vexx_home():
    produtos = Produtos.recuperar_produtos()
    categorias = Categoria.recuperar_categorias()
    return render_template("pagina_inicial.html", produtos = produtos, categorias = categorias)


@app.route('/catalogo/categoria')
def vexx_catalogo_categoria():
    return render_template("categoria_unica.html")



if __name__ == '__main__':
    app.run(debug=True) 