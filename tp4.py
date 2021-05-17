# Faire la fonction is_even(nb) -> bool
# Faire la fonction is_prime(nb) -> bool

x = 3
pi = 9

def add(nb, *kargs, **kwargs):
    sum = nb
    for value in kargs:
        sum += value
    return sum

def add_dico(nb, **args):
    sum = nb
    # for key, value in args:
    #     sum += value
    return sum

def is_even(nb: int) -> bool:
    return nb % 2 == 0

is_even = lambda nb: nb % 2 == 0 # nb € E -> bool

def is_prime(nb: int) -> bool:
    if nb <= 1:
        return False
    else:
        for div in range(2, int(nb ** 0.5) + 1):  # math.sqrt
            if nb % div == 0:
                return False
    return True

if __name__ == '__main__':
    print(is_even(2))
    print(is_prime(2))
    print(add(1,2,3,4))
    print(add_dico(nb=0, key1 = 0, key2 = 1))

    # f(x) = x + 1
    def f(x):
        return x + 1
    # <=>
    f = lambda x : x + 1

    print(f(3))
