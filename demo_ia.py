import pandas as pd
import matplotlib.pyplot as plt
# pip install scikit-learn
import sklearn.neural_network as nn
import sklearn.preprocessing as pp

pd.set_option('display.width', 160)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df = pd.read_csv("data/cancer/data.csv")

y = df["diagnosis"]
x = df.drop(["diagnosis", "id"], axis=1)

scaler = pp.StandardScaler()
scaler.fit(x) # Calculer sur toutes les colonnes mean et std
x = scaler.transform(x) # Appliques (x - mean) / std

model = nn.MLPClassifier(hidden_layer_sizes=(30,20,10))
model.fit(x, y)
print(model.score(x, y))

# print(df.corr())
plt.matshow(df.corr())
plt.show()