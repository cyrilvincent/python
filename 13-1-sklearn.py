import pandas as pd
import sklearn.linear_model as sklm
import sklearn.preprocessing as pp
import sklearn.pipeline as pipe

data = pd.read_csv('data/house.csv')
#regr = sklm.LinearRegression()
regr = pipe.make_pipeline(pp.PolynomialFeatures(3), sklm.Ridge())
X = data["surface"].values.reshape(-1,1)
y = data["loyer"]
regr.fit(X,y)
print(regr.predict(X))
print(regr.score(X, y))
# print(regr.coef_)
# print(regr.intercept_)

import numpy as np
import matplotlib.pyplot as plt
plt.plot(data["surface"], data["loyer"], 'ro', markersize=4)
plt.plot(np.arange(400), regr.predict(np.arange(400).reshape(-1,1)) )
plt.show()






