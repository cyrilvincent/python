# content = f.read()
# print(content)
import csv
import matplotlib.pyplot as plt
import pandas as pd

# with open("data/house/house.csv", "r") as f:
#     with open("data/house/test.csv", "w") as out:
#         for row in f:
#             out.write(row)

def load_csv(path):
    loyers = []
    surfaces = []
    with open(path) as f:
        reader = csv.DictReader(f, delimiter=',', lineterminator="\r\n")
        for row in reader:
            loyers.append(float(row["loyer"]))
            surfaces.append(float(row["surface"]))
    return loyers, surfaces


loyers, surfaces = load_csv("data/house/house.csv")
print(loyers)
print(surfaces)

dataframe = pd.read_csv("data/house/house.csv")
print(dataframe.loyer)
print(dataframe.surface)

plt.scatter(dataframe.surface, dataframe.loyer)
plt.show()

plt.scatter(surfaces, loyers)
plt.show()