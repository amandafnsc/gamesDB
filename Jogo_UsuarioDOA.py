import traceback
import psycopg2
from Jogo import Jogo
from Usuario import Usuario
from Connection import Connection

class JogoUsuarioDOA:
    def registrarAquisicao(self, id_usuario, nome_jogo, local, data_aquisicao, status):
        success = False
        try:
            connection = Connection.getConnection()
            cursor = connection.cursor()
            
            cursor.execute("SELECT id FROM jogo WHERE nome = %s", (nome_jogo,))
            result = cursor.fetchone()
            if result is None:
                print("Jogo não encontrado.")
                return False  # or raise an error

            jogo_id = result[0]

            cursor.execute("""
                INSERT INTO jogo_usuario (usuario_id, jogo_id, lugar, data_aquisicao, status)
                VALUES (%s, %s, %s, %s, %s)
            """, (id_usuario, jogo_id, local, data_aquisicao, status))

            connection.commit()
            success = cursor.rowcount == 1
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return success


        