def is_prime(x: int) -> bool:
    if x < 2:
        return False
    for div in range(2, x):
        if x % div == 0:
            return False
    return True

if __name__ == '__main__':
    print(is_prime(7))