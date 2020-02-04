import sqlite3

def rows_to_dict(cursor):
    columns = [i[0] for i in cursor.description]
    return [dict(zip(columns, row)) for row in cursor]

conn = sqlite3.connect("data/house.db3")
cursor = conn.cursor()
cursor.execute("select * from house")
dict = rows_to_dict(cursor)

l = [row["loyer"] / row["surface"] for row in dict]
print(sum(l) / len(l))

cursor.close()

# Calculer la surface moyenne
# Calculer le loyer moyen
# Calculer le loyer/m² moyen