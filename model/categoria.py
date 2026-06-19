from database.conexao import Conexao

class Categoria:
    @staticmethod
    def recuperar_categorias():
        conexao, cursor = Conexao.conectar()
        cursor.execute('SELECT codigo, imagem, nome FROM categorias')
        categorias = cursor.fetchall()
        conexao.close()
        return categorias
        
    @staticmethod
    def recuperar_categoria_por_id(id_categoria):
        conexao, cursor = Conexao.conectar()
        cursor.execute('SELECT codigo, imagem, nome FROM categorias WHERE codigo = %s', [id_categoria])
        categoria = cursor.fetchone()
        conexao.close()
        return categoria