from database.conexao import Conexao


class Produtos:
    def recuperar_produtos():
        conexao, cursor = Conexao.conectar()
        cursor.execute('SELECT codigo, nome, descricao, valor, foto, banner, categoria FROM produto')
        produtos = cursor.fetchall()
        return produtos
    
    def recuperar_produto_especifico(codigo):
        conexao, cursor = Conexao.conectar()
        cursor.execute('SELECT codigo, nome, descricao, valor, foto, banner, categoria FROM produto WHERE codigo = %s', [codigo])
        produto = cursor.fetchone()
        return produto
        