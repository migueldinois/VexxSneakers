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

@app.route('/cadastro')
def vexx_cadastro():
    return render_template("cadastro.html")


@app.route('/login')
def vexx_login():
    return render_template("login.html")
@app.route('/produtounico')
def vexx_produto_unico():
    return render_template("produto_especificacoes.html")

@app.route('/comentarios')
def vexx_comentarios():

    usuario = request.form.get("nome_usuario")
    comentario = request.form.get("comentario_usuario")

    comentario = 


    return render_template("produto_especificacoes.html")


if __name__=="__main__":
    app.run(debug=True)
