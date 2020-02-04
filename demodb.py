import sqlite3

def rows_to_dict(cursor):
    columns = [i[0] for i in cursor.description]
    return [dict(zip(columns, row)) for row in cursor]

conn = sqlite3.connect("data/house.db3")
cursor = conn.cursor()
cursor.execute("select * from house")
for row in rows_to_dict(cursor):
    print(row["surface"])
cursor.close()