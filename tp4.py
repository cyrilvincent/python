# Faire la fonction is_even(nb) -> bool
# Faire la fonction is_prime(nb) -> bool


def is_even(nb: int) -> bool:
    return nb % 2 == 0


def is_prime(nb: int) -> bool:
    if nb <= 1:
        return False
    else:
        for div in range(2, int(nb ** 0.5) + 1):  # math.sqrt
            if nb % div == 0:
                return False
    return True

print(is_even(2))
print(is_prime(2))