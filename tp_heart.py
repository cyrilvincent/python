import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/heartdisease/data_cleaned_up.csv")
# print(df.describe().T)
ok = df[df.num == 0]
ko = df[df.num == 1]

ok.to_excel("data/heartdisease/data.xlsx")

print(ok.describe().T)
print(ko.describe().T)

plt.scatter(ok.age, ok.chol, color="green")
plt.scatter(ko.age, ko.chol, color="red")
plt.show()

