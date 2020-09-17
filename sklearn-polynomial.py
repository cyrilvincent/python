import pandas as pd
import sklearn.linear_model as sklm

data = pd.read_csv('data/house.csv')
regr = sklm.LinearRegression()
X = data["surface"].values.reshape(-1,1)
y = data["loyer"]

import sklearn.model_selection as ms
xtrain, xtest, ytrain, ytest = ms.train_test_split(X, y, train_size=0.8, test_size=0.2)

import sklearn.preprocessing as pp
import sklearn.pipeline as pipe
model = pipe.make_pipeline(pp.PolynomialFeatures(4), sklm.Ridge())
model.fit(xtrain,ytrain)

import numpy as np
predict = model.predict(np.arange(400).reshape(-1,1))

print(model.score(xtest, ytest))

import matplotlib.pyplot as plt
plt.scatter(xtrain, ytrain)
plt.plot(range(400), predict)
print(model)
plt.show()