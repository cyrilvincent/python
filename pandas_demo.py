import pandas
import matplotlib.pyplot as plt

dataframe = pandas.read_csv("data/house.csv")
df_filter = dataframe[dataframe.surface < 200]
print(df_filter["loyer"] / df_filter.surface)

plt.scatter(df_filter.surface, df_filter["loyer"])
plt.show()