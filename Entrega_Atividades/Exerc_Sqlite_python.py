# 1 Importe o módulo sqlite3 e faça a conexão com o banco de dados escola_v2.db
# 2 Faça a query para pegar toda a tabela alunos e imprima na tela.
import sqlite3
from pathlib import Path

conec = sqlite3.Connection("MODULO 03/escola_v2.db")
cursor = conec.cursor()
# cursor.execute("""
#                SELECT *
#                FROM Aluno
#                """)
# print(cursor.fetchall())


# 3 Obtenha a media entre nota1 e nota2 dos alunos, ordene em ordem decrescente e retorne apenas os 10 maiores notas. No fim imprima na tela a lista desses alunos e suas médias.
# cursor.execute("""
# SELECT
#     id,
#     nome,
#     (nota1 + nota2) / 2 AS media_notas
# FROM
#     Aluno
# ORDER BY
#     media_notas DESC
# LIMIT 10;
# """)
# print(cursor.fetchall())


# 4 Use Left Join com as tabelas Aluno e Turma e imprima todos os dados da tabela.
# 5 Usando a query da questão 4, adicione um filtro para pegar apenas os alunos da turma 2 e imprima na tela.

# q = cursor.execute("SELECT * FROM Aluno")
# cursor.execute("""
#                SELECT *
#                FROM Aluno
#                LEFT JOIN Turma
#                ON id_turma = Turma.id
#                """)
# print(cursor.fetchall())

# q = cursor.execute("SELECT * FROM Aluno")
# cursor.



# def executar_query_e_imprimir(query: str, titulo: str):
#     print("-" * 50)
#     print(f"## {titulo}")
#     try:
#         conect = sqlite3.connect("MODULO 03/escola_v2.db")
#         cursor = conect.cursor()
        
#         cursor.execute(query)
#         resultados: List[Tuple] = cursor.fetchall()
        
#         if not resultados:
#             print("Nenhum resultado encontrado.")
#             return

#         if titulo == "1. Conteúdo Completo da Tabela Aluno":
#             colunas = [descricao[0] for descricao in cursor.description]
#             print(f"Colunas: {colunas}")

#         for linha in resultados:
#             print(linha)
            
#     except sqlite3.Error as e:
#         print(f"Ocorreu um erro de SQLite: {e}")
#     finally:
#         if 'conn' in locals() and conn:
#             conn.close()



# query_alunos = """
# SELECT * FROM Aluno;
# """
# executar_query_e_imprimir(query_alunos, "1. Conteúdo Completo da Tabela Aluno")

# query_left_join = """
# SELECT
#     A.*,
#     T.nome_turma,
#     T.id AS turma_id_turma_tabela
# FROM
#     Aluno AS A
# LEFT JOIN
#     Turma AS T ON A.turma_id = T.id;
# """
# executar_query_e_imprimir(query_left_join, "3. LEFT JOIN entre Aluno e Turma (Todos os Dados)")

# query_left_join_turma2 = """
# SELECT
#     A.*,
#     T.nome_turma,
#     T.id AS turma_id_turma_tabela
# FROM
#     Aluno AS A
# LEFT JOIN
#     Turma AS T ON A.turma_id = T.id
# WHERE
#     T.id = 2;
# """
# executar_query_e_imprimir(query_left_join_turma2, "4. LEFT JOIN: Apenas Alunos da Turma 2")

# print("-" * 50)
# print("Todas as consultas foram executadas.")