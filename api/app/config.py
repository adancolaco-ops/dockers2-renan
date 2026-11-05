
import os


class Config:
    DB_HOST = os.getenv("DB_HOST", "db")
    DB_PORT = os.getenv("DB_PORT", "5432")

    POSTGRES_USER = os.getenv("POSTGRES_USER", "calc")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "calc123")
    POSTGRES_DB = os.getenv("POSTGRES_DB", "calculadora")
