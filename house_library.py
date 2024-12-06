import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load(path):
    dataframe = pd.read_csv(path)
    return dataframe

def filter(dataframe, surface):
    return dataframe[dataframe.surface < surface]

def stats(dataframe):
    return np.mean(dataframe.surface), np.std(dataframe.surface), np.mean(dataframe.loyer), np.std(dataframe.surface)

def show(dataframe):
    plt.scatter(dataframe.surface, dataframe.loyer)
    plt.show()

if __name__ == '__main__':
    df = load("data/house/house.csv")
    df = filter(df, 200)
    print(stats(df))
    show(df)