import os

import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv, find_dotenv

from models.event import Event
from models.provider import Provider

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


def db_query(query: str):
    try:
        connection = get_db_connection()

        cursor = connection.cursor()

        cursor.execute(query)
        result = cursor.fetchall()

        return result
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
        return None
    finally:
        if connection:
            cursor.close()
            connection.close()


def get_event_ids_by_domain_name(domain_name: str) -> list[int]:
    domain_id = db_query(f"SELECT id FROM domain WHERE name = '{domain_name}'")[0][0]
    event_ids = db_query(f"SELECT e_id FROM event_domain WHERE d_id = {domain_id}")
    result = []
    for event_id in event_ids:
        result.extend(event_id)
    return result


def get_events_by_ids(event_ids: list[int]) -> list[Event]:
    events_result = db_query(f"SELECT * FROM event "
                             f"WHERE id IN ({str(event_ids)[1:-1]}) AND date > '2023-09-01' "
                             f"ORDER BY date")
    events = []
    for event in events_result:
        events.append(Event(
            id=event[0],
            m_id=event[1],
            p_id=event[2],
            original_text=event[3],
            title=event[4],
            long_desc=event[5],
            short_desc=event[6],
            date=event[7],
            time_b=event[8],
            time_e=event[9],
            place=event[10],
            geo_id=event[11],
            url=event[12],
            is_online=event[13],
            date_add=event[14],
            active=event[15]
        ))
    return events


def get_providers() -> list[Provider]:
    provider_result = db_query("SELECT * FROM provider")
    providers = []
    for provider in provider_result:
        providers.append(Provider(
            id=provider[0],
            url=provider[1],
            name=provider[2],
            description=provider[3],
            city=provider[4],
            address=provider[5],
            contacts=provider[6],
            date_add=provider[7],
            active=provider[8]
        ))
    return providers
