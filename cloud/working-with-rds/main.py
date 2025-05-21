"""A small example of connecting to a remote database."""

from os import environ as ENV, _Environ

from dotenv import load_dotenv
from psycopg2 import connect
from psycopg2.extensions import connection
from psycopg2.extras import RealDictCursor


def get_examples(conn: connection) -> list:
    """Returns all rows from the example table."""

    with conn.cursor() as cur:
        cur.execute("SELECT * FROM example;")
        data = cur.fetchall()

    return data


def get_db_connection(config: _Environ) -> connection:
    """Returns a live database connection."""

    return connect(
        cursor_factory=RealDictCursor,
        host=config["DB_HOST"],
        user=config["DB_USER"],
        password=config["DB_PASSWORD"],
        database=config["DB_NAME"]
    )

if __name__ == "__main__":

    load_dotenv()  # Read the details from a .env file into the environment
    
    conn = get_db_connection(ENV)

    print(get_examples(conn))
