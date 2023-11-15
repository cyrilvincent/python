import csv

# f = open("data/house/house.csv")
# s = f.read()
# print(s)
#
# with open("data/house/house.csv", "r") as f_in:
#     with open("data/house/house.tmp", "w") as f_out:
#         for row in f_in:
#             row = row.strip()
#             f_out.write(f"{row}\n")

with open("data/house/house.csv", "r") as f:
    reader = csv.DictReader(f)
    total = 0
    nb = 0
    for row in reader:
        total += float(row["loyer"])
        nb += 1
    avg = total / nb

import pickle
with open("data/house/house.pkl", "wb") as f:
    pickle.dump((avg, total), f)

avg = None

with open("data/house/house.pkl", "rb") as f:
    avg, total = pickle.load(f)
