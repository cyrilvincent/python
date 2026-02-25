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
import demo_tuple
import pickle

def get_loyer_m2(path):
    with open(path, "r") as f:
        loyer_m2 = []
        reader = csv.DictReader(f)
        for row in reader:
            value = float(row["loyer"])/float(row["surface"])
            loyer_m2.append(value)
    return loyer_m2

if __name__ == '__main__':
    loyer_m2 = get_loyer_m2("data/house/house.csv")
    with open("data/house/house.pkl", "wb") as f:
        pickle.dump(loyer_m2, f)
    with open("data/house/house.pkl", "rb") as f:
        loyer_m2 = pickle.load(f)
    min, max, avg = demo_tuple.min_max_avg(loyer_m2)
    print(min, max, avg)
# Afficher le min, max et avg
# Mettre ce code dans une jolie fonction

