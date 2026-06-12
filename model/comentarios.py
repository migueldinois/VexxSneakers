from database.conexao import Conexao


class Comentarios:
    def inserir_comentario(usuario, mensagem):
        try:
            conexao, cursor = Conexao.conectar()

            cursor.execute("""
                        INSERT INTO comentarios 
                                (usuario, mensagem) 
                        VALUES
                                (%s, %s);
                            """,
                            [usuario, mensagem]
                            )

            conexao.commit()
            conexao.close()

            return True
        except Exception as erro:
            print(erro)
            return False
        



