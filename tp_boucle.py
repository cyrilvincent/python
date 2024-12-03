# Faire une boucle de 0 à 10
# Faire une boucle de 10 à 0 inclus avec un pas de -2
# Multiplier entre eux tous les nombres de 1 à 10 => factorielle
# Afficher toutes la table des multiplications de 1 à 10 => 1*1=1, 1*2=2, .... 5*6=30, 10*10=100
# Pas facile : afficher la suite de fibonacci de 15 => f(15) = 610
# Bonus : Afficher si n est premier sauf s'il possède un diviseur entre 2 et n-1

for i in range(10,-1,-1):
    print(i)

factorielle = 1
for i in range(2,11):
    factorielle *= i
print(factorielle)

a = 1
b = 0
for i in range(2, 15):
    fibo = a + b
    b = a
    a = fibo
print(fibo)

for i in range(1,11):
    for j in range(1, 11):
        print(f"{i}*{j}={i*j}")

n = 1223
for div in range(2, int(n ** 0.5) + 1):
    if n % div == 0:
        print("Non premier")
        break
print("Premier")
