from database.conexao import Conexao

class Usuarios():
    def cadastrar_usuario(nome, email, telefone, endereco, senha):
        try:
            conexao, cursor = Conexao.conectar()

            cursor.execute("""INSERT INTO usuarios(nome, email, telefone, endereco, senha)VALUES(%s, %s, %s, %s, %s)""", [nome, email, telefone, endereco, senha])
            conexao.commit()
            conexao.close()
            return True
        except Exception as erro:
            print(erro)
            return False
        
    @staticmethod
    def verificar_usuario(email:str, senha:str) -> dict:
        try:
            conexao, cursor = Conexao.conectar()

            cursor.execute("""SELECT nome, email from usuarios where email = %s AND senha = %s""", [email, senha])
            usuario = cursor.fetchone()
            conexao.commit()
            conexao.close()
            return usuario


        except Exception as erro:
            print(erro)
            return False