import sqlite3

with sqlite3.connect("data/books.db3") as conn:
    cursor = conn.cursor()
    cursor.execute("select id, title, price from book")
    for row in cursor:
        print(row[1])

