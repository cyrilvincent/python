import numpy as np

print(np.__version__)

a1 = np.array([1,2,3,4])
print(a1)
a2 = np.full(10, 2, dtype="float")
print(a2)
print(a2.dtype)

a3 = np.arange(0,1,0.1)
print(a3)
a4 = np.linspace(0,1,11)
print(a4)

a5 = np.random.rand(10)
print(a5)
a6 = np.random.randint(0,100,10)
print(a6)

print(a1.size, a1.ndim, a1.shape)

a1 = np.array([1,2,3,4])
print(a1 * 2)
a2 = np.array([10,20,30,40])
print(a1 * a2)
a1 = a2
a1 = a1 + 1
print(a1, a2)
# a3 = np.array([1,2,3])
# print(a1 + a3)

print(np.sin(a1))
rnd = np.random.rand(10)
rnd = rnd * 20 - 10
print(rnd)

print(np.sum(a1), np.max(a1))
rnd = np.random.rand(1000000)
print(np.mean(rnd), np.std(rnd), np.median(rnd))

a1 = np.arange(100)
print(a1[1::2])
print(a1[55::-3])

np.savez("data.npz", a1=a1, a2=a2)
content = np.load("data.npz")
print(content.keys())
a1 = content["a1"]
a2 = content["a2"]

# TP
# Retrouver les surfaces et loyers de house.csv
# Afficher la size, ndim, shape et dtype des tableaux
# Calculer la moyenne et l'écart type des surfaces et loyers
# Créer le tableau loyer_per_m2
# Sauvegarder les 3 tableaux dans un .npz
# Calculer le loyer_per_m2 moyen + ecart type
