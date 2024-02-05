# Avec un while afficher les chiffres pairs de 0 à 100
# Avec un for afficher les multiples de 3 de 99 à 0
# Avec 2 while afficher la table des additions de 0 à 10
# Avec 2 for afficher la table de multiplication de 0 à 10
# Saisir un chiffre
# Dire s'il et premier ou non
# n est premier sauf s'il possède un diviseur compris entre 2 et n-1
# BONUS : afficher les 100 premiers nombres premiers

i = 0
while i<100:
    print(i)
    i += 2

for i in range(99,-1,-3):
    print(i)

i = 1
while i<=10:
    j = 1
    while j<=10:
        print(f"{i}+{j}={i+j}")
        j += 1
    i += 1

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i}*{j}={i*j}")

nb = 1223
is_prime = True
if nb < 2:
    is_prime = False
else:
    for div in range(2, nb):
        if nb % div == 0:
            is_prime = False
            break
print(f"Est prime: {is_prime}")

