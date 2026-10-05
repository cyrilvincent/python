i = 0
j = 0
while i < 10:
    while j < 10:
        print(f"{i}*{j}={i * j}")
        j += 1
    i += 1
    j = 0

i = 0
while i < 10:
    print(i)
    i += 1

for i in range(10):
    for j in range(10):
        print(f"{i}*{j}={i * j}")

total = 0
nb_max = 100
for i in range(nb_max):
    total += i
print(total)

for i in range(5,18,3):
    print(i)

# TP
# Créer tp_boucle
# Refaire la somme de 0 à 9 inclus avec un while
# Créer la factorielle n! = 1*2*3*4*...*n 5! = 5*4*3*2*1 = 120
# Bonus : Fibonacci

