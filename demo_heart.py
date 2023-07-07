import pandas as pd

dataframe = pd.read_csv("data/heartdisease/data_cleaned_up.csv")
dataframe_ok = dataframe[dataframe.num == 0]
dataframe_ko = dataframe[dataframe.num == 1]

print(dataframe_ok.describe().T)
print(dataframe_ko.describe().T)
