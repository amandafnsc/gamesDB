import traceback
import psycopg2
from Jogo import Jogo
from Connection import Connection


class JogoDOA:

    def listarJogos(self):
        resultado = []
        try:
            connection = Connection.getConnection()
            cursor = connection.cursor()
            cursor.execute("SELECT id, nome FROM jogo")
            registros = cursor.fetchall()
            for linha in registros:
                u = Jogo()
                u.id = linha[0]
                u.nome = linha[1]
                resultado.append(u)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return resultado
    
    def inserirJogo(
        self, nome, descricao, idioma, duracao, tipo,
        min_jogadores, max_jogadores,
        nome_categoria, nome_editora
    ):
        success = False
        try:
            connection = Connection.getConnection()
            cursor = connection.cursor()

            cursor.execute("SELECT id FROM categoria WHERE nome = %s", (nome_categoria,))
            categoria = cursor.fetchone()
            if categoria:
                id_categoria = categoria[0]
            else:
                cursor.execute("INSERT INTO categoria (nome) VALUES (%s) RETURNING id", (nome_categoria,))
                id_categoria = cursor.fetchone()[0]

            cursor.execute("SELECT id FROM editora WHERE nome = %s", (nome_editora,))
            editora = cursor.fetchone()
            if editora:
                id_editora = editora[0]
            else:
                cursor.execute("INSERT INTO editora (nome) VALUES (%s) RETURNING id", (nome_editora,))
                id_editora = cursor.fetchone()[0]

            cursor.execute("""
                INSERT INTO jogo (
                    nome, descricao, idioma, duracao, tipo,
                    min_jogadores, max_jogadores,
                    id_categoria, id_editora
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                nome, descricao, idioma, duracao, tipo,
                min_jogadores, max_jogadores,
                id_categoria, id_editora
            ))

            connection.commit()
            success = cursor.rowcount == 1

        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return success


    def atualizarJogo(
    self, jogo_id, nome, descricao, idioma, duracao, tipo,
    min_jogadores, max_jogadores,
    nome_categoria, nome_editora
    ):
        success = False
        try:
            connection = Connection.getConnection()
            cursor = connection.cursor()

            # Verifica ou insere categoria
            cursor.execute("SELECT id FROM categoria WHERE nome = %s", (nome_categoria,))
            categoria = cursor.fetchone()
            if categoria:
                id_categoria = categoria[0]
            else:
                cursor.execute("INSERT INTO categoria (nome) VALUES (%s) RETURNING id", (nome_categoria,))
                id_categoria = cursor.fetchone()[0]

            # Verifica ou insere editora
            cursor.execute("SELECT id FROM editora WHERE nome = %s", (nome_editora,))
            editora = cursor.fetchone()
            if editora:
                id_editora = editora[0]
            else:
                cursor.execute("INSERT INTO editora (nome) VALUES (%s) RETURNING id", (nome_editora,))
                id_editora = cursor.fetchone()[0]

            # Atualiza o jogo
            cursor.execute("""
                UPDATE jogo SET
                    nome = %s,
                    descricao = %s,
                    idioma = %s,
                    duracao = %s,
                    tipo = %s,
                    min_jogadores = %s,
                    max_jogadores = %s,
                    id_categoria = %s,
                    id_editora = %s
                WHERE id = %s
            """, (
                nome, descricao, idioma, duracao, tipo,
                min_jogadores, max_jogadores,
                id_categoria, id_editora,
                jogo_id
            ))

            connection.commit()
            success = cursor.rowcount == 1

        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return success


    def deletarJogo(self, id):
        sucess = False
        try:
            connection = Connection.getConnection()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM jogo WHERE id = %s", (id,))
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
    
    def buscarJogoPorNome(self, nome):
        resultado = []
        try:
            connection = Connection.getConnection()
            cursor = connection.cursor()
            cursor.execute("""
                SELECT j.id, j.nome, j.descricao, j.duracao, j.tipo, 
                    j.min_jogadores, j.max_jogadores,
                    c.nome AS categoria_nome,
                    e.nome AS editora_nome
                FROM jogo j
                JOIN categoria c ON j.id_categoria = c.id
                JOIN editora e ON j.id_editora = e.id
                WHERE j.nome ILIKE %s
            """, (nome,))
            registros = cursor.fetchall()
            for linha in registros:
                u = Jogo()
                u.id = linha[0]
                u.nome = linha[1]
                u.descricao = linha[2]
                u.duracao = linha[3]
                u.tipo = linha[4]
                u.min_jogadores = linha[5]
                u.max_jogadores = linha[6]
                u.categoria = linha[7]
                u.editora = linha[8]
                resultado.append(u)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return resultado

    
    def buscarJogoPorCategoria(self, categoria):
        resultado = []
        try:
            connection = Connection.getConnection()
            cursor = connection.cursor()
            cursor.execute("""
                SELECT j.id, j.nome, j.descricao, j.duracao, j.tipo, 
                    j.min_jogadores, j.max_jogadores,
                    c.nome AS categoria_nome,
                    e.nome AS editora_nome
                FROM jogo j
                JOIN categoria c ON j.id_categoria = c.id
                JOIN editora e ON j.id_editora = e.id
                WHERE c.nome ILIKE %s
            """, (categoria,))
            registros = cursor.fetchall()
            for linha in registros:
                u = Jogo()
                u.id = linha[0]
                u.nome = linha[1]
                u.descricao = linha[2]
                u.duracao = linha[3]
                u.tipo = linha[4]
                u.min_jogadores = linha[5]
                u.max_jogadores = linha[6]
                u.categoria = linha[7]
                u.editora = linha[8]
                resultado.append(u)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return resultado
    

    
    def buscarJogoPorEditora(self, editora):
        resultado = []
        try:
            connection = Connection.getConnection()
            cursor = connection.cursor()
            cursor.execute("""
                SELECT j.id, j.nome, j.descricao, j.duracao, j.tipo, 
                    j.min_jogadores, j.max_jogadores,
                    c.nome AS categoria_nome,
                    e.nome AS editora_nome
                FROM jogo j
                JOIN categoria c ON j.id_categoria = c.id
                JOIN editora e ON j.id_editora = e.id
                WHERE e.nome ILIKE %s
            """, (editora,))
            registros = cursor.fetchall()
            for linha in registros:
                u = Jogo()
                u.id = linha[0]
                u.nome = linha[1]
                u.descricao = linha[2]
                u.duracao = linha[3]
                u.tipo = linha[4]
                u.min_jogadores = linha[5]
                u.max_jogadores = linha[6]
                u.categoria = linha[7]
                u.editora = linha[8]
                resultado.append(u)
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            if connection:
                cursor.close()
                connection.close()
        return resultado

