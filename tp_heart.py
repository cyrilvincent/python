import pandas as pd

dataframe = pd.read_csv("data/heart/data_cleaned_up.csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
print(dataframe.describe())

# Créer le dataframe ok qui contient les num==0
# Créer le dataframe ko qui contient les num==1
# Afficher les describe(), en déduire des choses sur chol, trestbps, thalach?

dataframe = dataframe.drop(["cp", "fbs", "exang", "oldpeak", "restecg"], axis=1)

ok = dataframe[dataframe["num"]==0]
ko = dataframe[dataframe["num"]==1]

print(ok.describe())
print(ko.describe())

print(dataframe.corr())