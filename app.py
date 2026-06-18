from flask import Flask, render_template, request, redirect, session
from model.produtos import Produtos
from model.categoria import Categoria
from model.usuarios import Usuarios
from model.comentarios import Comentarios
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
    
    if session.get("usuario_logado") is not None:
        return redirect('/')  
    else:
        return render_template("cadastro.html")  

@app.route("/cadastrar", methods=["POST"])
def cadastrar():

    input_nome = request.form.get("nome")
    input_email = request.form.get("email")
    input_telefone = request.form.get("telefone")
    input_cep = request.form.get("cep")
    input_senha = request.form.get("senha")
    
    resposta = Usuarios.verificar_usuario(input_email, input_senha)

    if resposta is not None:
        session["usuario_logado"] = resposta
        return redirect("/")
    else:
        return render_template("cadastro.html", erro="Erro ao cadastrar.")

@app.route('/login')
def vexx_login():
    if session.get("usuario_logado") is not None:
        return redirect('/')  
    else:
        return render_template("login.html")  

@app.route('/produtounico/<codigo_produto>')
def vexx_produto_unico(codigo_produto):
    produto = Produtos.recuperar_produto_especifico(codigo_produto)
    comentarios_produto = Comentarios.visualizar_comentario(codigo_produto)
    if produto is not None:
        return render_template("produto_especificacoes.html", produto = produto, comentarios=comentarios_produto)
    else: 
        return render_template("404.html")


@app.route('/comentar', methods=['POST'])
def comentarios():
    texto = request.form.get("comentario")

    resposta = Comentarios.inserir_comentario(texto)
    print(resposta)

        
@app.route('/logar', methods=['POST'])
def logar():
    input_email = request.form.get("email")
    input_senha = request.form.get("senha")

    resposta = Usuarios.verificar_usuario(input_email, input_senha)
    
    if resposta is not None:
        session["usuario_logado"] = resposta
        return redirect("/")
    else:
        return render_template("login.html", erro="Usuário ou senha incorretos")


@app.route('/logout')
def logout():
    session.pop("usuario_logado", None)
    return redirect("/")



@app.route('/categoria_unica')
def categoria_unica():
    
    return render_template("categoria_unica.html")

@app.route("/musica/post", methods=["POST"])
def api_inserir_url_catalogo():

    nome_categoria = request.form.get("")


if __name__=="__main__":
    app.run(debug=True)
