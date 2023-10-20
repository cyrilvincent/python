# Comprendre demo_file
# Réutiliser la fonction load_csv
# Calculer moyenne min max
# Avec le zip de demo_zip créer la fonction qui retourne la liste des prix au m²
# Calculer moyenne min max

# for loyer, surface in zip(loyers, surfaces)

import demo_file
import demo_tuple

def get_loyers_per_m2(loyers, surfaces):
    res = []
    for loyer, surface in zip(loyers, surfaces):
        res.append(loyer / surface)
    return res


loyers, surfaces = demo_file.load_csv("data/house/house.csv")
min, max, avg = demo_tuple.min_max_avg(loyers)
print(min, max, avg)
min, max, avg = demo_tuple.min_max_avg(surfaces)
print(min, max, avg)
loyers_m2 = get_loyers_per_m2(loyers, surfaces)
print(loyers_m2)
min, max, avg = demo_tuple.min_max_avg(loyers_m2)
print(min, max, avg)


