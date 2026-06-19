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
    
    resposta = Usuarios.cadastrar_usuario(input_nome, input_email, input_telefone, input_cep, input_senha)

    if resposta:
        session["usuario_logado"] = {"nome": input_nome, "email": input_email}
        return redirect("/")
    else:
        return render_template("cadastro.html", erro="Erro ao cadastrar.")

@app.route('/login')
def vexx_login():
    if session.get("usuario_logado") is not None:
        return redirect('/')  
    else:
        return render_template("login.html")  

@app.route('/produto/<codigo_produto>')
def vexx_produto_unico(codigo_produto):
    produto = Produtos.recuperar_produto_especifico(codigo_produto)
    comentarios_produto = Comentarios.visualizar_comentario(codigo_produto)
    if produto is not None:
        return render_template("produto_especificacoes.html", produto = produto, comentarios=comentarios_produto)
    else: 
        return render_template("404.html")


@app.route('/comentar/<codigo_produto>', methods=['POST'])
def comentarios(codigo_produto):
    if session.get("usuario_logado") is None:
        return redirect('/login')
        
    usuario = session["usuario_logado"]
    nome_usuario = usuario["nome"]
    
    texto = request.form.get("comentario")
    if texto:
        Comentarios.inserir_comentario(codigo_produto, nome_usuario, texto)
        return redirect(f"/produto/{codigo_produto}")
    else:
        produto = Produtos.recuperar_produto_especifico(codigo_produto)
        comentarios_produto = Comentarios.visualizar_comentario(codigo_produto)
        return render_template('produto_especificacoes.html', erro='Não foi possível enviar seu comentário.', produto=produto, comentarios=comentarios_produto)

        
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



@app.route('/categoria/<id_categoria>')
def categoria_unica(id_categoria):
    categoria = Categoria.recuperar_categoria_por_id(id_categoria)
    nome_categoria = categoria["nome"]
    produtos = Produtos.recuperar_produtos_de_categoria(id_categoria)
    
    return render_template("categoria_unica.html", produtos=produtos, nome_categoria=nome_categoria)




if __name__=="__main__":
    app.run(debug=True)
