# Condition
# Saisir votre age et afficher votre catégroei d'age
# < 1 an : BB
# < 12 ans : enfant
# < 18 ans : ado
# < 64 ans : actif
# < 100 ans : retraité
# sinon : grand age

# Boucle
# Faire une boucle de 0 à 100 inclus
# Faire un compte à rebours de 10 à 0
# Afficher tous les multiples de 3 inférieurs à 100

# Additionner tous les nombres de 1 à n, par exemple n=5 => 1+2+3+4+5 => 15

# Bonus
# Soit x un entier > 0
# Afficher True si x est premier
# Tous nombre x >= 2 est premier sauf s'il possède un diviseur entre 2 et x-1

age = 20
if age < 1:
    print("BB")
elif age < 12:
    print("Enfant")
elif age < 18:
    print("Ado")
else:
    print("Adulte")

for i in range(11):
    print(i)

for i in range(10,-1,-1):
    print(i)

for i in range(0,10,3):
    print(i)

n = 5
sum = 0
for i in range(1, n+1):
    sum = sum + i
print(sum)

x = 8
is_prime = True
for div in range(2, int(x ** 0.5) + 1):
    if x % div == 0:
        is_prime = False
        break
print(is_prime)