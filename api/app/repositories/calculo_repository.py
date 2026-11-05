
from app.database import get_connection


class CalculoRepository:

    # Salvar um cálculo
    @staticmethod
    def salvar(calculo):
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO calculos
                    (operacao, a, b, resultado)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id, operacao, a, b, resultado, criado_em;
                """, (
                    calculo.operacao,
                    calculo.a,
                    calculo.b,
                    calculo.resultado
                ))

                item = cursor.fetchone()
                connection.commit()

                return {
                    "id": item[0],
                    "operacao": item[1],
                    "a": item[2],
                    "b": item[3],
                    "resultado": item[4],
                    "criado_em": item[5].isoformat()
                }
        finally:
            connection.close()

    # Listar cálculos com filtro e limite
    @staticmethod
    def listar(operacao=None, limite=None):
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                query = """
                    SELECT id, operacao, a, b, resultado, criado_em
                    FROM calculos
                """

                filtros = []
                parametros = []

                if operacao:
                    filtros.append("operacao = %s")
                    parametros.append(operacao)

                if filtros:
                    query += " WHERE " + " AND ".join(filtros)

                query += " ORDER BY id DESC"

                if limite is not None:
                    query += " LIMIT %s"
                    parametros.append(limite)

                cursor.execute(query, parametros)

                resultados = cursor.fetchall()

                return [
                    {
                        "id": item[0],
                        "operacao": item[1],
                        "a": item[2],
                        "b": item[3],
                        "resultado": item[4],
                        "criado_em": item[5].isoformat()
                    }
                    for item in resultados
                ]
        finally:
            connection.close()

    # Buscar cálculo pelo ID
    @staticmethod
    def buscar_por_id(id):
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id, operacao, a, b, resultado, criado_em
                    FROM calculos
                    WHERE id = %s;
                """, (id,))

                item = cursor.fetchone()

                if item is None:
                    return None

                return {
                    "id": item[0],
                    "operacao": item[1],
                    "a": item[2],
                    "b": item[3],
                    "resultado": item[4],
                    "criado_em": item[5].isoformat()
                }
        finally:
            connection.close()

    # Resumo dos cálculos
    @staticmethod
    def resumo():
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT
                        COUNT(*),
                        SUM(resultado),
                        AVG(resultado)
                    FROM calculos;
                """)

                item = cursor.fetchone()

                return {
                    "total_calculos": item[0],
                    "soma_resultados": float(item[1]) if item[1] is not None else 0,
                    "media_resultados": float(item[2]) if item[2] is not None else 0
                }
        finally:
            connection.close()

    # Excluir cálculo pelo ID
    @staticmethod
    def excluir_por_id(id):
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM calculos
                    WHERE id = %s
                    RETURNING id;
                """, (id,))

                resultado = cursor.fetchone()
                connection.commit()

                return resultado is not None
        finally:
            connection.close()

    # Excluir todo o histórico
    @staticmethod
    def excluir_todos():
        connection = get_connection()

        try:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM calculos;")
                quantidade = cursor.rowcount
                connection.commit()

                return quantidade
        finally:
            connection.close()
