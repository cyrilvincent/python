# Faire la fonction is_even(x)=> True or False
# Faire la fonction us_prime(x) => True et False
#Tester

def is_even(x):
    return x % 2 == 0

def is_prime(x):
    res = True
    for div in range(2, int(x ** 0.5 + 1)):
        if x % div == 0:
            res = False
            break
    return res

if __name__ == '__main__':
    print(is_even(7))
    print(is_prime(7))
