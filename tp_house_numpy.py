import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

dico = np.load("data/house/house.npz")
print(dico["loyers"], dico["surfaces"])

# Afficher pour loyers, le max, le min, sum/len
# Créer le vecteur loyer_m2 = loyers/surfaces
# Filtrer les surfaces < 200
# Bonus : Filtrer les loyers dont la surface < 200

loyers = dico["loyers"]
surfaces = dico["surfaces"]

print(np.min(loyers), np.max(loyers), np.sum(loyers)/len(loyers))
loyer_m2 = loyers / surfaces
print(np.min(loyer_m2), np.max(loyer_m2), np.sum(loyer_m2)/len(loyer_m2))
surfaces_inf100 = surfaces[surfaces < 100]
print(surfaces_inf100)
loyers_inf100 = loyers[surfaces < 100]
print(loyers_inf100)
print(surfaces[loyers < 1000])
print(loyers < 1000)

print(np.mean(loyers), np.std(loyers), np.var(loyers), np.median(loyers), np.quantile(loyers, [0.01, 0.1, 0.25, 0.5, 0.75, 0.9, 0.99]))

slope, intercept, rvalue, pvalue, _ = stats.linregress(surfaces, loyers)
print(slope, intercept, rvalue, pvalue)

plt.subplot(2,1,1)
plt.scatter(surfaces, loyers)
plt.plot(surfaces, slope * surfaces + intercept, color="red")
plt.title("house")
# plt.show(block = False)

slope, intercept, rvalue, pvalue, _ = stats.linregress(surfaces[surfaces<178], loyers[surfaces<178])
print(slope, intercept, rvalue, pvalue)

plt.subplot(2,1,2)
plt.title(f"house filtered {slope:.2f}")
plt.scatter(surfaces[surfaces < 178], loyers[surfaces < 178])
plt.plot(surfaces, slope * surfaces + intercept, color="red")
plt.show()
