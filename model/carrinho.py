from database.conexao import Conexao

class Carrinho():
    @staticmethod
    def recuperar_carrinho(usuario: str) -> list:
        conexao, cursor = Conexao.conectar()
        cursor.execute("""
            SELECT c.cod_carrinho, u.email, i.quantidade, p.nome, p.valor, p.foto
            FROM carrinhos c
            INNER JOIN usuarios u ON c.usuario = u.email
            INNER JOIN itens_carrinho i ON c.cod_carrinho = i.cod_carrinho
            INNER JOIN produto p ON p.codigo = i.cod_produto
            WHERE u.email = %s AND c.finalizado = 0
        """, [usuario])
        produtos = cursor.fetchall()
        conexao.close()
        return produtos

    @staticmethod
    def adicionar_item_carrinho(cod_produto, cod_carrinho, quantidade=1):
        try:
            conexao, cursor = Conexao.conectar()
            cursor.execute("""
                INSERT INTO itens_carrinho (cod_produto, cod_carrinho, quantidade) 
                VALUES (%s, %s, %s);
            """, [cod_produto, cod_carrinho, quantidade])
            conexao.commit()
            conexao.close()
            return True        
        except Exception as erro:
            print(erro)
            return False
        
    @staticmethod
    def verificar_carrinho_aberto(usuario: str):
        try:
            conexao, cursor = Conexao.conectar()
            cursor.execute('SELECT cod_carrinho FROM carrinhos WHERE usuario = %s AND finalizado = 0 LIMIT 1', [usuario])
            carrinho = cursor.fetchone()
            conexao.close()
            
            if carrinho:
                # retorna o primeiro item da lista que no caso é o codigo
                return carrinho[0] 
            return None
        except Exception as erro:
            print(f"Erro no banco: {erro}")
            return None


    @staticmethod
    def criar_carrinho_novo(usuario: str):
        conexao = None
        try:
            conexao, cursor = Conexao.conectar()
            cursor.execute("INSERT INTO carrinhos(usuario, finalizado) VALUES(%s, 0)", [usuario])
            conexao.commit()
            id_carrinho = cursor.lastrowid 
            return id_carrinho
        except Exception as erro:
            print(f"Erro ao criar carrinho: {erro}")
            return False
        finally:
            if conexao:
                conexao.close()

    @staticmethod
    def deletar_item_carrinho(cod_item_carrinho, cod_carrinho):
        try:
            conexao, cursor = Conexao.conectar()
            cursor.execute("""
                DELETE FROM itens_carrinho 
                WHERE cod_item_carrinho = %s AND cod_carrinho = %s
            """, [cod_item_carrinho, cod_carrinho])
            conexao.commit()
            conexao.close()
            return True        
        except Exception as erro:
            print(erro)
            return False
        
    