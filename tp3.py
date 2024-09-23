# Créer la fonction max(i: float, j: float) -> float
# Créer la fonction factorielle(n:int) -> int 5! = 1*2*3*4*5
# Créer la fonction is_prime(n: int) -> bool
# Bonus : afficher tous les nombres premiers < 100

def max(i:float, j:float) -> float:
    if i > j:
        return i
    else:
        return j

def fact(n:int) -> int:
    total = 1
    for i in range(1, n+1):
        total *= i
    return total

def is_prime(n:int) -> bool:
    if n > 1:
        for div in range(2, int(n ** 0.5) + 1):
            if n % div == 0:
                return False
        return True
    else:
        return False


print(max(3,2))
print(fact(5))
print(is_prime(9), is_prime(13))
for i in range(100000000):
    if is_prime(i) == True:
        print(i)
