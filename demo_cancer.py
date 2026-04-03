import sklearn.neural_network as neural
import sklearn.preprocessing as pp
import pandas as pd

df = pd.read_csv("data/cancer/data.csv")
y = df["diagnosis"]
x = df.drop(["diagnosis","id"], axis=1)

scaler = pp.RobustScaler()
scaler.fit(x)
x = scaler.transform(x)

model = neural.MLPClassifier(hidden_layer_sizes=(30,20,10), max_iter=1000)
model.fit(x, y)
ypred = model.predict(x)
print(model.score(x, y))