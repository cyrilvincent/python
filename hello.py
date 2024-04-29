print("Hello World!")

s = input("Saisir x: ")
x = int(s)


def is_prime(x: int) -> bool:
    if x > 1:
        for div in range(2, x):
            if x % div == 0:
                return False
        return True
    return False


print(is_prime(x))



