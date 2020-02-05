import pandas as pd
import sklearn.linear_model as sklm
import sklearn.pipeline as pipe
import sklearn.preprocessing as pp


data = pd.read_csv('data/house.csv')
regr = sklm.LinearRegression()
#regr = pipe.make_pipeline(pp.PolynomialFeatures(3), sklm.Ridge())
X = data["surface"].values.reshape(-1,1)
y = data["loyer"]

import sklearn.model_selection as ms
xtrain, xtest,ytrain,ytest = ms.train_test_split(X, y, train_size=0.8, test_size=0.2)
regr.fit(xtrain,ytrain)
print(regr.predict(xtest))
print(regr.score(xtest, ytest))
print(regr.coef_)
print(regr.intercept_)

import matplotlib.pyplot as plt
plt.plot(data["surface"], data["loyer"], 'ro', markersize=4)
plt.scatter(data["surface"], regr.predict(X) )
plt.show()