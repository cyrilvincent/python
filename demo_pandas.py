import pandas as pd
import numpy as np

dataframe = pd.read_csv("data/house/house.csv")
dataframe["loyer_per_m2"] = dataframe.loyer / dataframe.surface
print(np.mean(dataframe["loyer_per_m2"]))
print(dataframe.describe())