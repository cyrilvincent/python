import numpy as np
import demo_file

loyers, surfaces = demo_file.parse_house_csv("data/house/house.csv")

loyers = np.array(loyers)
print(np.min(loyers), np.max(loyers), np.median(loyers), np.mean(loyers), np.std(loyers))

loyers_m2 = loyers / surfaces
print(np.min(loyers_m2), np.max(loyers_m2), np.median(loyers_m2), np.mean(loyers_m2), np.std(loyers_m2))


# Faire les stats sur loyers & surfaces
# Créer le array loyer_m2
# Faire les stats sur loyer_m2

