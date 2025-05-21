from os import environ as ENV

from psycopg2 import connect
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

if __name__ == "__main__":

    load_dotenv()

    with connect(dbname=ENV['DB_NAME'],
                 cursor_factory=RealDictCursor) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM pokemon WHERE pokemon_name ILIKE '%ez%';")
            data = cur.fetchall()

    for row in data:
        print(row)

    conn.close()