import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

rnd = np.random.rand(1000)
rnd_y = np.random.rand(1000)
print(np.mean(rnd), np.std(rnd), np.var(rnd), np.median(rnd), np.quantile(rnd, [0.01, 0.1, 0.25, 0.5, 0.75, 0.9, 0.99]))

plt.scatter(rnd, rnd_y)

slope, intercept, rvalue, pvalue, stderr = stats.linregress(rnd, rnd_y)
print(slope, intercept, rvalue, pvalue, stderr)
plt.plot(rnd, slope * rnd + intercept, color="red")
plt.show()

# Pour house
# Calculer les moyenne ecart types, mediane, quantiles des loyers
# Calculer et afficher la regression lineaire pour toutes les surfaces puis pour les surfaces < 178