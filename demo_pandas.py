import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("data/house/house.csv")
dataframe = dataframe[dataframe.surface < 180]
loyer = dataframe["loyer"]
surface = dataframe.surface
loyer_per_m2 = loyer / surface
dataframe["loyer_per_m2"] = loyer_per_m2
print(dataframe)
dataframe.to_json("data/house/house.json", indent=4)
dataframe.to_xml("data/house/house.xml",pretty_print=True,root_name="loyers",row_name="loyer")
dataframe.to_excel("data/house/house.xlsx")
plt.scatter(surface, loyer)
plt.show()

