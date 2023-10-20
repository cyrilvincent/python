# Comprendre demo_file
# Réutiliser la fonction load_csv
# Calculer moyenne min max
# Avec le zip de demo_zip créer la fonction qui retourne la liste des prix au m²
# Calculer moyenne min max

# for loyer, surface in zip(loyers, surfaces)


import demo_file
import demo_tuple
import pickle

def get_loyers_per_m2(loyers, surfaces):
    res = []
    for loyer, surface in zip(loyers, surfaces):
        res.append(loyer / surface)
    return res

def save(x, path):
    with open(path, "wb") as f:
        pickle.dump(x, f)



def load(path):
    with open(path, "rb") as f:
        loyers_m2 = pickle.load(f)
        return loyers_m2

loyers, surfaces = demo_file.load_csv("data/house/house.csv")
min, max, avg = demo_tuple.min_max_avg(loyers)
print(min, max, avg)
min, max, avg = demo_tuple.min_max_avg(surfaces)
print(min, max, avg)
loyers_m2 = get_loyers_per_m2(loyers, surfaces)
print(loyers_m2)
min, max, avg = demo_tuple.min_max_avg(loyers_m2)
print(min, max, avg)


save(loyers_m2, "data/house/house.pkl")
# with open("data/house/house.pkl", "wb") as f:
#     pickle.dump(loyers_m2, f)

loyers_m2 = None

loyers_m2 = load("data/house/house.pkl")

# with open("data/house/house.pkl", "rb") as f:
#     loyers_m2 = pickle.load(f)
#     print(loyers_m2)

# tp_pickle créer les fonctions load et save




