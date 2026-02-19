import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import scipy.optimize as opt

# Creer la bd access
# Dans panneau de configuration > odbc > Créer une source de données utilisateur
# pip install pyodbc sqlalchemy sqlalchemy-access openpyxl


dataframe = pd.read_csv("data/house/house.csv", )
print(dataframe.dtypes)
dataframe["loyer_m2"] = dataframe["loyer"]/dataframe["surface"]
print(dataframe)
print(dataframe.describe())

# dataframe.to_excel("data/house/house.xlsx")
# dataframe.to_sql("house", r"access+pyodbc://@house" )




# Filter les data pour les surfaces < 100m²

print(np.mean(dataframe["loyer"]), np.std(dataframe["loyer"]), np.median(dataframe["loyer"]), np.quantile(dataframe["loyer"], [0.1,0.25,0.5,0.75,0.9]))

slope, intercept, rvalue, pvalue, stderr = stats.linregress(dataframe["surface"], dataframe["loyer"])

def poly2(x, a, b, c):
    return a * x ** 2 + b * x + c

weights, convs = opt.curve_fit(poly2, dataframe["surface"], dataframe["loyer"])
print(weights)
print(convs)


x = np.arange(400)
y = slope * x + intercept

print(slope, intercept, rvalue, pvalue, stderr)

plt.scatter(dataframe["surface"], dataframe["loyer"])
plt.plot(x, y, color="red")
plt.plot(x, poly2(x, weights[0], weights[1], weights[2]), color="black")
plt.show()

