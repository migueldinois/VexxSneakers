from flask import Flask, render_template, request, redirect, session
from model.produtos import Produtos
from model.categoria import Categoria
from model.usuarios import Usuarios
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

@app.route('/logar', methods=['POST'])
def logar():
    input_email = request.form.get("email")
    input_senha = request.form.get("senha")

    resposta = Usuarios.verificar_usuario(input_email, input_senha)
    print(resposta)
    if resposta != None:
        session["usuario_logado"] = resposta
        return redirect("/")
    else:
        print("Usuario ou senha incorretos")
        return redirect("/login")
    

if __name__ == '__main__':
    app.run(debug=True) 