# Afficher les nombre pairs < 100 (x%2==0)
# Afficher la table des multiplications <= 10
# Refaire la factorielle
# Pour tous les nombres n < 100, si n est pair affiche le carré du nombre sinon afficher sa racine carrée ** 0.5
# Calculer le nieme nombre de la suite de fibonacci (par exemple pour n=10 => 55)
# Bonus : Dire si n est premier ou non, n > 0 et entier est premier ssi il possède 2 diviseurs 1 et lui même
#   Tout nombre n > 0 est premier SAUF s'il possède un diviseur entre 2 et n-1

for i in range(0,100,2):
    print(i)

for a in range(11):
    for b in range(11):
        print(f"{a}*{b}={a*b}")

for i in range(100):
    if i%2 == 0:
        print(i ** 2)
    else:
        print(f"{i ** 0.5:.2f}")

f0 = 0
f1 = 1
n = 15
fn = f1
for i in range(n-1):
    fn = f0 + f1
    f0 = f1
    f1 = fn
print(f"F({n})={fn}")

n=1223
is_prime=True
for div in range(2, int(n ** 0.5) + 1):
    if n % div == 0:
        is_prime=False
        break
print(f"{n} is prime: {is_prime}")

