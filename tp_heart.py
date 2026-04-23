# Lire dans un df data/heart/data_cleaned_up.csv
# Créer le df ok pour les num==0
# Créer le df ko pour les num==1
# afficher un describe pour ok & ko
# que peut on en déduire sur age, sex, trestbps, thalach et chol
# tester df.corr() = Pearson

import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
df = pd.read_csv("data/heart/data_cleaned_up.csv")
ok = df[df["num"] == 0]
ko = df[df["num"] == 1]

print(ok.describe())
print(ko.describe())

print(df.corr(method="pearson"))
