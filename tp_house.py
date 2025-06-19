import numpy as np
import unittest

data = np.load("data/house/house.npz")
print(data)


loyers = data["loyers"]
surfaces = data["surfaces"]

filter = surfaces < 100
loyers_filter = loyers[filter]
surfaces_filter = surfaces[filter]
loyer_m2 = loyers_filter / surfaces_filter
print(np.mean(loyer_m2), np.median(loyer_m2), np.std(loyer_m2))


loyers_filter[:100:2]

# Retrouver loyers & surfaces
# Recalculer loyer_m2
# Filtrer surface < 100
# Faire les stats de base