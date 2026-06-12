from database.conexao import Conexao


class Comentarios:
    def adicionar_avaliacao():

        conexao, cursor = Conexao.conectar()

        cursor.execute('INSERT usuario, mensagem FROM comentarios')

        Comentarios = cursor.fetchall()

        return Comentarios
        



