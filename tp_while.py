# Afficher tous les nombres pairs < 100
# Décrémenter de 100 à 0 ave un pas de -6
# Afficher i**2 pour tous les i <= 16
# Soit n=5, calculer n! 5!=5*4*3*2*1=120

# i = 0
# while i < 100:
#     print(i)
#     i += 2

# i = 100
# while i >= 0:
#     print(i)
#     i -= 6

# i = 0
# while i <= 16:
#     print(2 ** i)
#     i += 1

n = 5
i = 1
while n > 1:
    i = i * n
    n -= 1
print(i)
