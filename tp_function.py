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
    """
    Retourne True si x est premier
    """
    a = 4
    if x < 2:
        return False
    for div in range(2, int(x ** 0.5) + 1):
        if x % div == 0:
            return False
    return True


if __name__ == '__main__':
    print("TOTO")
    print(is_even(2154679))
    res = is_prime(13)
    print(res)
    