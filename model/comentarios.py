from database.conexao import Conexao


class Comentarios:
    def inserir_comentario(id_produto, usuario, mensagem):
        try:
            conexao, cursor = Conexao.conectar()

            cursor.execute("""
                        INSERT INTO comentarios 
                                (id_produto, usuario, mensagem) 
                        VALUES
                                (%s, %s, %s);
                            """,
                            [id_produto, usuario, mensagem]
                            )

            conexao.commit()
            conexao.close()

            return True
        except Exception as erro:
            print(erro)
            return False
        

    def visualizar_comentario(codigo_produto):
        conexao, cursor = Conexao.conectar()

        cursor.execute("""
                        SELECT id_produto, usuario, mensagem FROM comentarios WHERE id_produto = %s;

                        """, [codigo_produto])
        

        comentarios = cursor.fetchall()
        conexao.close()
        return comentarios
        



