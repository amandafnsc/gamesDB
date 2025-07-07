import traceback
import psycopg2
from Connection import Connection
from Usuario import Usuario

class UsuarioDAO:
    def listarUsuarios(self):
        resultado = []
        try:
            connection = Connection.getConnection()
            cursor = connection.cursor()
            cursor.execute("SELECT id, nome, email FROM usuario")
            registros = cursor.fetchall()
            for linha in registros:
                u = Usuario()
                u.id = linha[0]
                u.nome = linha[1]
                u.email= linha[2]
                resultado.append(u)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return resultado
    
    def inserirUsuario(self, nome, email, senha):
        sucess = False
        try:
            connection = Connection.getConnection()
            cursor = connection.cursor()
            cursor.execute("INSERT INTO usuario (nome, email, senha) VALUES ('{}', '{}', '{}')".format(nome, email, senha))
            connection.commit()
            if cursor.rowcount == 1:
                sucess = True       
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucess

    
    def atualizarUsuario(self, nome, email, senha):
        sucess = False
        try:
            connection = Connection.getConnection()
            cursor = connection.cursor()
            cursor.execute("UPDATE usuario SET nome = '{}', login = '{}', senha = '{}')".format(nome, email, senha))
            connection.commit()
            if cursor.rowcount == 1:
                sucess = True       
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucess
    
    def deletarUsuario (self, id):
        sucess = False
        try:
            connection = Connection.getConnection()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM usuario WHERE id = %s", (id,))
            connection.commit()
            if cursor.rowcount == 1:
                sucess = True       
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return sucess


