import numpy as np
import pandas
import matplotlib.pyplot as plt
import sklearn.neural_network as nn
import sklearn.model_selection as ms
import sklearn.preprocessing as preprocess

data = pandas.read_csv("data/cancer.csv", index_col="id")
y = data.diagnosis
x = data.drop("diagnosis", axis=1)

scaler = preprocess.StandardScaler()
scaler.fit(x)
x = scaler.transform(x)

np.random.seed(0)
xtrain, xtest, ytrain, ytest = ms.train_test_split(x,y,train_size=0.08, test_size=0.02)

# array = np.random.rand(100)
# truefalse = array[array > 0.5]
# y[truefalse]

model = nn.MLPClassifier(hidden_layer_sizes=(30,20))
model.fit(xtrain, ytrain)
predict = model.predict(xtest) - ytest
print(predict.values)
print(model.score(xtest, ytest))