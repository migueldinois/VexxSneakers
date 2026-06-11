from database.conexao import Conexao


class Categoria:
    def recuperar_categorias():
        conexao, cursor = Conexao.conectar()
        cursor.execute('SELECT codigo, imagem, nome FROM categorias')
        categorias = cursor.fetchall()
        return categorias
        