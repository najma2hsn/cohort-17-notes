from sqlite3 import connect

if __name__ == "__main__":

    conn = connect("chinook.db")

    with open("c1.sql", 'r') as f:
        q = f.read()

    cur = conn.cursor()
    cur.execute(q)
    data = cur.fetchall()

    # other processing...