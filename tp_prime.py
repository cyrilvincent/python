# Créer la fonction is_prime(x:int) -> bool
# Si x < 2 False
# i % 2 == 0 => i est pair

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    is_prime = True
    for div in range(2, n):
        if n % div == 0:
            is_prime = False
            break
    return is_prime

if __name__ == '__main__':
    assert is_prime(7) == True
    assert is_prime(8) == True


