# Afficher les nb pairs de 0 à 100
# Afficher un compte à rebours de 10 à 0 inclus
# Saisir n (entier)
# Calculer n! : 5! = 1 * 2 * 3 * 4 * 5
# Dire si N est premier
# Bonus : Tout nombre > 1 est premier sauf s'il possède un diviseur entre 2 et n-1

# i = 0
# while i < 100:
#     print(i)
#     i+=2
#
# i = 10
# while i >= 0:
#     print(i)
#     i -= 1

# n = 4
# i = 1
# res = 1
# while i <= n:
#     res *= i
#     i += 1
# print(res)

n = 2147483647
is_prime = True
if n<2:
    is_prime = False
else:
    diviseur = 2
    while diviseur < n ** 0.5 + 1:
        if n % diviseur == 0:
            is_prime = False
            break
        diviseur += 1
    print(is_prime)



