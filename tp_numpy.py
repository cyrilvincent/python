import numpy as np
import demo_file

loyers, surfaces = demo_file.parse_house_csv("data/house/house.csv")

loyers = np.array(loyers)
print(np.median(loyers), np.mean(loyers), np.std(loyers))

# Faire les stats sur loyers & surface
# Créer le tableau loyer_m2
# Faire les stats sur loyer_m2

