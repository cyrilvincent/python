#1 Saisir un entier
#2 Afficher s'il est premier ou non

x = int(input("x: "))

isPrime = x >= 2
if isPrime:
    for i in range(2,int(x ** 0.5 + 1)):
        if x % i == 0:
            isPrime = False
            break

print(f"{x} is primer number: {isPrime}")
