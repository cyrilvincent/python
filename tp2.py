# Reprendre tp1
# Créer la fonction is_prime(x) -> True or False

__version__ = 1.0
__author__ = "Cyril"

def is_prime(x: int) -> bool:
    if x < 2:
        return False
    else:
        res = True
        for div in range(2, x):
            if x % div == 0:
                res = False
                break
        return res

if __name__ == '__main__':
    print(is_prime(7))
    print(is_prime(8))

