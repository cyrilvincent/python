def add(x=0,y=0):
    """
    Add x y
    :param x: first argument
    :param y: second argument
    :return: x + y
    """
    return x + y

z = add(2,3)
z = add(x = 2, y = 3)
z = add(2)
z = add(2, y = 0)

# 1 Créer la fonction isEven(x)
# 2 Créer la fonction isPrime(x)
# 3 Refaire la question 1 avec une lambda

def isEven(x):
    return x % 2 == 0

isEven2 = lambda x : x % 2 == 0

def isPrime(x):
    res = x >= 2
    if res:
        for i in range(2, int(x ** 0.5 + 1)):
            if x % i == 0:
                res = False
                break
    return res

if __name__ == '__main__':
    print(isEven(8))
    print(isEven2(8))
    print(isPrime(7))