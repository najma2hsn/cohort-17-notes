"""A small example of communicating with an SQLite database."""

from sqlite3 import connect

if __name__ == "__main__":

    conn = connect("chinook.db")

    cur = conn.cursor()

    cur.execute("SELECT * FROM customers;")

    data = cur.fetchall()

    cur.close()
    conn.close()

    print(data)