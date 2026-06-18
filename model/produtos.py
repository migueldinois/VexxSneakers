from database.conexao import Conexao


class Produtos:
    def recuperar_produtos():
        conexao, cursor = Conexao.conectar()
        cursor.execute('SELECT codigo, nome, descricao, valor, foto, banner, categoria FROM produto')
        produtos = cursor.fetchall()
        return produtos
        