import pandas as pd
import numpy as np
import sklearn.ensemble as rf
import sklearn.model_selection as ms
import sklearn.metrics as metrics
import matplotlib.pyplot as plt
import sklearn.neural_network as nn
import sklearn.preprocessing as pp

dataframe = pd.read_csv("data/cancer/data.csv", index_col="id")
print(dataframe.describe().T)
y = dataframe.diagnosis # dataframe["diagnosis"]
x = dataframe.drop("diagnosis", axis=1)

np.random.seed(42)
xtrain, xtest, ytrain, ytest = ms.train_test_split(x, y, train_size=0.8, test_size=0.2)

scaler = pp.RobustScaler()
scaler.fit(xtrain)
xtrain = scaler.transform(xtrain)
xtest = scaler.transform(xtest)


#model = rf.RandomForestClassifier(n_estimators=100)
model = nn.MLPClassifier(hidden_layer_sizes=(30,30))
model.fit(xtrain, ytrain)
ypred = model.predict(xtest)
score = model.score(xtrain, ytrain)
print(score)
score = model.score(xtest, ytest)
print(score)
#print(model.feature_importances_)

# plt.bar(x.columns, model.feature_importances_)
# plt.xticks(rotation=45)
# plt.show()



print(metrics.classification_report(ytest, ypred))
print(metrics.confusion_matrix(ytest, ypred))
