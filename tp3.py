def add(x: float, y: float = 0, z: float = 0) -> float:
    return x + y + z

add = lambda x,y,z : x + y + z

# f(x) = x + 1
f = lambda x : x + 1

toto = add

# 1/ Faire la fonction isEven(x) qui retourne vrai si x est pair
# 2/ Faire la fonction isPrime(x) qui retourne vrai si x est premier
# 3/ Afficher les nombres premiers < 100
# 4/ refaire la question 1/ en lambda

def isEven(x:int)->bool:
    """
    toto
    :param x: tata
    :return:
    """
    return x % 2 == 0

def isPrime(nb: int)->bool:
    res = True
    if nb < 2:
        res = False
    for div in range(2, int((nb ** 0.5)) + 1):
        if nb % div == 0:
            res = False
            break
    return res

def showPrimes(max = 100):
    for i in range(max):
        if isPrime(i):
            print(i)



isEven = lambda x: x % 2 == 0

if __name__ == '__main__':
    print(toto(1,2,3))
    print(f(2))
    showPrimes(1000000)