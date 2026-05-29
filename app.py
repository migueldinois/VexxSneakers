from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'Vexx777@'

@app.route('/')
def vexx_home():
    return render_template("pagina_inicial.html")


@app.route('/categoria')
def vexx_categoria():
    return render_template("categoria.html")


if __name__ == '__main__':
    app.run(debug=True) 