# # f = open("data/house/house.csv", "r")
# # content = f.read()
# # print(content)
#
# # f = open("data/house/house.db3", "rb")
# # content = f.read()
#
# f = open("data/house/house.csv", "r")
# for row in f:
#     print(row.strip())
#
# w = open("data/house/fake.txt", "w")
# w.write("toto\ntiti\n")
#
# with open("data/house/house.csv", "r") as f:
#     with open("data/house/house2.csv", "w") as w:
#         for row in f:
#             w.write(row)
#
import csv

with open("data/house/house.csv", "r") as f:
    loyer_m2 = []
    reader = csv.DictReader(f)
    for row in reader:
        loyer_m2.append(float(row["loyer"])/float(row["surface"]))

print(loyer_m2)

# Afficher le min, max et avg
# Mettre ce code dans une jolie fonction

