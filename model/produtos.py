from database.conexao import Conexao


class Produtos:
    def recuperar_produtos():
        conexao, cursor = Conexao.conectar()
        cursor.execute('SELECT codigo, nome, descricao, valor, foto, banner, categoria FROM produto')
        produtos = cursor.fetchall()
        return produtos
    
    def recuperar_produtos_de_categoria(id_categoria):

        conexao, cursor = Conexao.conectar()
        cursor.execute('SELECT codigo, nome, descricao, valor, foto, banner, categoria FROM produto WHERE categoria = %s ',
                       [id_categoria])
        produtos = cursor.fetchall()
        return produtos