import pandas as pd
import sklearn.linear_model as sklm
import sklearn.neighbors as nn
import sklearn.ensemble as rf



from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer() # more info : https://goo.gl/U2Uwz2

#input
X=cancer['data']
y=cancer['target']

print(X.shape) #569 * 30
print(y.shape) #569

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y)

model = rf.RandomForestClassifier(n_estimators=100)
model.fit(X_train,y_train)

import pickle
with open("data/forest.pickle", "wb") as f:
    pickle.dump(model, f)

print(model.feature_importances_)
print(model.score(X_test, y_test))
predict = model.predict(X_test)
print(predict - y_test)