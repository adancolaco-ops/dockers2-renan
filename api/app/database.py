
import psycopg2

from app.config import Config


def get_connection():
    return psycopg2.connect(
        host=Config.DB_HOST,
        port=Config.DB_PORT,
        user=Config.POSTGRES_USER,
        password=Config.POSTGRES_PASSWORD,
        dbname=Config.POSTGRES_DB
    )


def init_db():
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS calculos (
                    id SERIAL PRIMARY KEY,
                    operacao VARCHAR(20) NOT NULL,
                    a DOUBLE PRECISION NOT NULL,
                    b DOUBLE PRECISION NOT NULL,
                    resultado DOUBLE PRECISION NOT NULL,
                    criado_em TIMESTAMP NOT NULL DEFAULT NOW()
                );
            """)

        connection.commit()

    finally:
        connection.close()
