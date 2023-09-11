import os

import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
DATABASE_NAME = os.environ.get('DATABASE_NAME')
DATABASE_USER = os.environ.get('DATABASE_USER')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
DATABASE_HOST = os.environ.get('DATABASE_HOST')
DATABASE_PORT = os.environ.get('DATABASE_PORT')


def get_db_connection():
    return psycopg2.connect(
        database=DATABASE_NAME,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        host=DATABASE_HOST,
        port=DATABASE_PORT
    )


def db_query(query):
    try:
        connection = get_db_connection()

        cursor = connection.cursor()
        postgresql_query = query

        cursor.execute(postgresql_query)
        result = cursor.fetchall()

        return result
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
        return None
    finally:
        if connection:
            cursor.close()
            connection.close()
