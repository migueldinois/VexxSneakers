from database.conexao import Conexao

class Produtos:
    @staticmethod
    def recuperar_produtos():
        conexao, cursor = Conexao.conectar()
        cursor.execute('SELECT codigo, nome, descricao, valor, foto, banner, categoria FROM produto')
        produtos = cursor.fetchall()
        conexao.close()
        return produtos
        
    @staticmethod
    def recuperar_produto_especifico(codigo):
        conexao, cursor = Conexao.conectar()
        cursor.execute('SELECT codigo, nome, descricao, valor, foto, banner, categoria FROM produto WHERE codigo = %s', [codigo])
        produto = cursor.fetchone()
        conexao.close()
        return produto

    @staticmethod
    def recuperar_produtos_de_categoria(id_categoria):
        conexao, cursor = Conexao.conectar()
        cursor.execute('SELECT codigo, nome, descricao, valor, foto, banner, categoria FROM produto WHERE categoria = %s', [id_categoria])
        produtos = cursor.fetchall()
        conexao.close()
        return produtos

    @staticmethod
    def recuperar_produto_por_id(id_produto):
        return Produtos.recuperar_produto_especifico(id_produto)