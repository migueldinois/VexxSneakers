from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'Vexx777@'

@app.route('/')
def vexx_home():
    return render_template("pagina_inicial.html")


@app.route('/catalogo/categoria')
def vexx_catalogo_categoria():
    return render_template("categoria_unica.html")

@app.route('/cadastro')
def vexx_cadastro():
    return render_template("cadastro.html")

if __name__ == '__main__':
    app.run(debug=True) 