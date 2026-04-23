import pandas as pd
import matplotlib.pyplot as plt
import datetime
# pip install openpyxl

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
df = pd.read_csv("data/house/house.csv")
plt.scatter(df["surface"], df["loyer"])
df["loyer_m2"] = df["loyer"] / df["surface"]
print(df)
df.to_html("data/house/house.html")
now = datetime.datetime.now()

df.to_excel(f"data/house/house_{now.year}{now.month}{now.day}{now.hour}{now.minute}.xlsx", index=False)
plt.show()