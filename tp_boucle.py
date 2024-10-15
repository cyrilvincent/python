# Afficher les nb de 0 à 9
# Afficher un compte à rebours de 10 à 0 inclus
# Sommer les nombre de 0 à 100
# Calculer la factorielle 5! = 5*4*3*2*1
# Bonus : Calculer la factorielle de n
# Bonus : Calculer le nieme terme de la suite de fibonacci = 0 1 1 2 3 5 8 13
# Hyper bonus : Dire si un nombre est premier
# Tout nombre n est premier si est > 1 ET sauf s'il possède un diviseur entre 2 et n-1

for i in range(10):
    print(i)

for i in range(10,-1,-1):
    print(i)

total = 0
for i in range(101):
    total += i
print(total)

fact = 1
n = 6
for i in range(n,0,-1):
    fact *= i
print(fact)

a = 0
b = 1
n = 15
for i in range(n - 1):
    fibo = a + b
    a = b
    b = fibo
print(fibo)

n = 999

if n > 1:
    is_prime = True
    for i in range(2,n):
        if n % i == 0:
            is_prime = False
            break
    print(is_prime)

