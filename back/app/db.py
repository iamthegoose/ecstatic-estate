
import json
from pydantic import BaseModel, ConfigDict
import psycopg2
from settings import settings


try:
    connection = psycopg2.connect(
        dbname=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD.get_secret_value(),
        host=settings.DB_HOST,
        port=settings.DB_PORT
    )

    connection.set_client_encoding('UTF8')

    cursor = connection.cursor()

    cursor.execute("SHOW client_encoding;")
    client_encoding = cursor.fetchone()

    cursor.execute("SELECT version();")

    record = cursor.fetchone()
    print(f"connected to  {record[0]}\n")

    print(f"coding -  {client_encoding[0]}\n")

    print(f"disconnected from {record[0]}")
    cursor.close()
    connection.close()
except (psycopg2.Error) as error:
    print(f"Помилка при підключенні до PostgreSQL: {error}")


# class Response(BaseModel):
#     world: str
#     name: str


# b = Response.model_validate(a)

# print(b.world)
