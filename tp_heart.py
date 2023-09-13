import pandas as pd

df = pd.read_csv("data/heartdisease/data_cleaned_up.csv")
# print(df.describe().T)
ok = df[df.num == 0]
ko = df[df.num == 1]

print(ok.describe().T)
print(ko.describe().T)