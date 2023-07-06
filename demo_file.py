import csv
from typing import Tuple, List
import tp6
import matplotlib.pyplot as plt
import scipy.stats as stats

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

# save_house_pickle(loyers, surfaces):
#t = (loyers, surfaces) => data/house/house.pickle

# load_house_pickle(path) -> Tuple[List[float], List[float]]

if __name__ == '__main__':
    loyers, surfaces = parse_house_csv("data/house/house.csv")
    print(loyers)
    print(tp6.average(loyers), tp6.average(surfaces))
    slope, intercept, rvalue, pvalue, loss = stats.linregress(surfaces, loyers)
    y = [slope * x + intercept for x in surfaces]
    plt.plot(surfaces, y, color="red")
    plt.scatter(surfaces, loyers)
    plt.show()
