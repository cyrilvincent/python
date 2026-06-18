# Saisir un nb avec input et caster en int
# Afficher nb²
# Afficher sa factorielle 5! = 5 * 4 * 3 * 2 * 1 = 120
# Calculer 2**nb sans utiliser l'opérateur ** 
# Difficile : fibo(nb) fibo(10)=55
# Très difficile : afficher si nb est premier tout nb >= 2 est premier SAUF s'il possède un diviseur entre 2 et nb-1

nb = int(input("Saisir nb : "))
print(nb ** 2)

# facto = 1
# for i in range(2, nb + 1):
#     facto *= i
# print(f"F({nb})={facto}")


f0 = 0
f1 = 1
fibo = 0
for _ in range(nb - 1):
    fibo = f0 + f1
    f0 = f1
    f1 = fibo
print(f"Fibo({nb})={fibo}")

is_prime = True
if nb < 2:
    is_prime = False
else:
    for div in range(2, nb):
        if nb % div == 0:
            is_prime = False
            break
print(f"{nb} is prime number: {is_prime}")

