import pandas as pd
import matplotlib.pyplot as plt

# data/climate/
# pd.read_csv(index_col="nom_col")
# Alléger le dataframe prendre 1 ligne à midi tous les jours
# Faire un describe + pd.set_option('display.max_columns', None)
# Afficher dans matplotlib les plots des T (degC), des p (mbar) et Tdew (degC)
# Ajouter la colonne mist True False

dataframe = pd.read_csv("data/climate/jena_filtered.csv", index_col="Date Time")
dataframe = dataframe[11::24]
pd.set_option("display.max_columns", None)
print(dataframe.describe().T)

dataframe["mist"] = dataframe["T (degC)"] <= dataframe["Tdew (degC)"]
print(dataframe[dataframe["mist"]])

plt.subplot(221)
plt.plot(dataframe.index, dataframe["p (mbar)"])
plt.xticks([])
plt.subplot(222)
plt.plot(dataframe.index, dataframe["T (degC)"])
plt.xticks([])
plt.subplot(223)
plt.plot(dataframe.index, dataframe["Tdew (degC)"])
plt.xticks([])
plt.subplot(224)
plt.plot(dataframe.index, dataframe["rh (%)"])
plt.xticks([])
plt.show()
