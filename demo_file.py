import csv
import json
from typing import Tuple, List
import tp6
import matplotlib.pyplot as plt
import scipy.stats as stats
import pickle

def parse_house_csv(path: str) -> Tuple[List[float], List[float]]:
    loyers = []
    surfaces = []
    with open(path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            loyer = float(row['loyer'])
            surface = float(row["surface"])
            loyers.append(loyer)
            surfaces.append(surface)
    return loyers, surfaces

def save_house_pickle(path, loyers, surfaces):
    with open(path, "wb") as f:
        t = (loyers, surfaces)
        pickle.dump(t, f)

def load_house_pickle(path):
    with open(path, "rb") as f:
        return pickle.load(f)

def save_house_json(path, loyers, surfaces):
    with open(path, "w") as f:
        t = (loyers, surfaces)
        json.dump(t, f,indent="\t\"")

def load_house_json(path):
    with open(path, "r") as f:
        return json.load(f)



if __name__ == '__main__':
    # loyers, surfaces = parse_house_csv("data/house/house.csv")
    # save_house_pickle("data/house/house.pickle", loyers, surfaces)
    loyers, surfaces = load_house_pickle("data/house/house.pickle")
    save_house_json("data/house/house.json", loyers, surfaces)
    print(loyers)
    print(tp6.average(loyers), tp6.average(surfaces))
    slope, intercept, rvalue, pvalue, loss = stats.linregress(surfaces, loyers)
    y = [slope * x + intercept for x in surfaces]
    plt.plot(surfaces, y, color="red")
    plt.scatter(surfaces, loyers)
    plt.show()
