from database.conexao import Conexao


class Comentarios:
    def inserir_comentario(mensagem):
        try:
            conexao, cursor = Conexao.conectar()

            cursor.execute("""
                        INSERT INTO comentarios 
                                (mensagem) 
                        VALUES
                                (%s);
                            """,
                            [mensagem]
                            )

            conexao.commit()
            conexao.close()

            return True
        except Exception as erro:
            print(erro)
            return False
        



