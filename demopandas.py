import pandas as pd
import sqlite3
#df = pd.read_csv("data/house.csv")
with sqlite3.connect("data/house.db3") as conn:
    df = pd.read_sql("select * from house", conn)
print(df.head())
#print(df.loyer)