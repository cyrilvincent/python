def add(i,j):
    return i + j

def inc(i):
    return i + 1

inc = lambda x : x + 1

def isEven(i):
    return i % 2 == 0

def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

toto = isPrime

if __name__ == '__main__':
    print(isEven(7))
    print(isEven(8))
    print(isPrime(7))
    print(isPrime(7789))

    print(isEven(2) and isPrime(2))
    print(type(isEven))
