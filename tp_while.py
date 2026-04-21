# Afficher tous les nb pairs < 100
# Sommer touts les nombre compris entre 1 et 10
# afficher la table des multiplications
# Difficile : Calculer n!, par exemple 5! = 2 * 3 * 4 * 5 = 120
# Très difficile : Calculer F(n) où F est la suite de fibonacci
# Hyper difficile : Pour n>=2 dire si n est premier

i = 0
while i < 100:
    print(i)
    i += 2

sum = 0
i = 1
while i <= 10:
    sum += i
    i += 1
print(sum)

i = 0
j = 0
while i <= 10:
    while j <= 10:
        print(f"{i}x{j}={i * j}")
        j += 1
    i += 1
    j = 0

n = 5
result = 1
i = 2
while i <= n:
    result *= i
    i += 1
print(f"{n}!={result}")

n = 10
f0 = 0
f1 = 1
i = 2
result = 0
while i <= n:
    result = f0 + f1
    f0 = f1
    f1 = result
    i += 1
print(f"F({n})={result}")

n = 7919
i = 2
if n < 2:
    is_prime = False
else:
    is_prime = True
    while i < n:
        if n % i == 0:
            is_prime = False
        i += 1
    print(is_prime)



