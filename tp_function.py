# Faire la fonction is_even(x:int) -> bool
# Faire la fonction is_prime(x: int) -> bool
# Bonus : Afficher tous les nombres premiers < 1000

def is_even(x: int) -> bool:
    """
    slrkgjrmdjgndrmkjgnrsfdmjn
    """
    if x % 2 == 0:
        return True
    else:
        return False
    
def is_prime(x: int) -> bool:
    if x < 2:
        return False
    for div in range(2, x ** 0.5 + 1):
        if x % div == 0:
            return False
    return True
    
print(is_even(2154679))
res = is_prime(6)
print(res)