# Afficher les nombres pairs de 0 à 100
# Afficher un compte à rebours de 10 à 0 inclus
# Saisir un nombre et afficher s'il est pair ou impair ( x % 2 == 0 => True ou False)
# Saisir un chiffre et dire s'il est premier ou non

for i in range(0,100,2):
    print(i)

for i in range(10,-1,-1):
    print(i)

x = int(input("nb: "))
if x % 2 == 0:
    print("Pair")
else:
    print("Impair")

is_prime = True
for div in range(2, int(x ** 0.5 + 1)):
    if x % div == 0:
        is_prime = False
        break
if is_prime == True:
    print("Premier")
else:
    print("Non premier")
