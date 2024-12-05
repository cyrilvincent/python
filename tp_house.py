import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import scipy.optimize as opt

data = np.load("data/house/house.npz")
print(data)
loyers = data["loyers"]
surfaces = data["surfaces"]
print(loyers.shape, surfaces.shape)
print(loyers)

# Afficher min, max, sum(loyers) / len(loyers) pour loyers & surfaces
# loyers_m2, puis afficher min, max, moy
# Créer la fonction qui modélise cela : f(surface) = loyer_m2_moyen * surface

print(np.min(loyers), np.max(loyers))
loyers_m2 = loyers / surfaces
print(np.min(loyers_m2), np.max(loyers_m2), np.sum(loyers_m2) / len(loyers_m2))

def model_loyer(surfaces):
    return surfaces * 37.66

slope, intercept, rvalue, pvalue, stderr = stats.linregress(surfaces, loyers)
print(slope, intercept)

def poly2(x, a,b,c):
    return a*x**2 + b*x + c

weights, loss = opt.curve_fit(poly2, surfaces, loyers)



surfaces_filtered = surfaces[surfaces < 200]
loyers_filtered = loyers[surfaces < 200]

mean = np.mean(loyers_filtered)
std = np.std(loyers_filtered)
print(mean, std)

surfaces_filtered = surfaces_filtered[loyers_filtered < mean + 3 * std]
loyers_filtered = loyers_filtered[loyers_filtered < mean + 3 * std]




plt.subplot(211)
x = np.arange(400)
y = model_loyer(x)
plt.scatter(surfaces, loyers)
plt.plot(x, slope * x + intercept, color="green")
plt.plot(x, y, color="red")
plt.plot(x, poly2(x, weights[0], weights[1], weights[2]), color="black")

plt.subplot(212)

slope, intercept, rvalue, pvalue, stderr = stats.linregress(surfaces_filtered, loyers_filtered)
print(slope, intercept)
x = np.arange(200)
plt.plot(x, slope * x + intercept, color="black")

plt.scatter(surfaces_filtered, loyers_filtered)
plt.show()



if __name__ == '__main__':
    print(model_loyer(100))

# Afficher le nuage de points surfaces / loyers
# Afficher le model_loyer
# Regression lineaire
# Regression poly2
# calculer moyenne et ecart type des surfaces
# Bonus filtrer avec [] les surfaces > 200 & > 3 ecarts types
# Bonus refaire les regressions