# Afficher les nb pairs < 100
# Refaire par vous même la table de multiplication
# Soit un n un nombre entier par exmple n=5 calculer sa factorielle 5!=5*4*3*2*1
# Difficile : Soit n=5 calculer fibo(5) Wiki fibonacci
# Difficile++ : Dire si n est premier ou non : Tout nb > 1 est premier sauf s'il possède un diviseur entre 2 et nb-1

# i = 0
# while i < 100:
#     print(i)
#     i += 2

# n = 4
# i = 2
# facto = 1
# while i <= n:
#     facto = facto * i
#     i += 1
# print(f"{n}!={facto}")
#
# f0 = 0
# f1 = 1
# i = 1
# n = 15
# fibo = 0
# while i<n:
#     fibo = f0 + f1
#     f0 = f1
#     f1 = fibo
#     i += 1
# print(fibo)

n = 1223
is_prime = True
div = 2
while div < n:
    if n % div == 0:
        is_prime = False
        break
    div += 1
if is_prime:
    print(f"{n} est premier")
else:
    print(f"{n} n'est pas premier")

