# Boucler de 0 à 100
# Boucler de 100 à 0 avec un pas de -3
# Calculer la factorielle de n=5 => 5*4*3*2*1
# Dire si n=7 est premier => Un nb est preier s'il possède 2 diviseurs : 1 et lui même n
# Cherche si n possède un diviseur entre 2 et n-1, n % 3 == 0

n=5
res=1
for i in range(2,n+1):
    res *= i
print(f"{n}!={res}")

n=7919
if n < 2:
    print("Non premier")
else:
    found = True
    for div in range(2,n):
        if n % div == 0:
            print("Non premier")
            found = False
            break
    if found:
        print("Premier")
