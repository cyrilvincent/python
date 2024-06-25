# Programmer un module
# Tester dans le module puis tester dans un main.py
# Refaire la fonction sum et tester
# Faire la fonction average
# Faire les fonctions min, max
# Faire la fonction sum_even qui somme que les nombres pairs
# Bonus : palindrome(l) -> bool ex: 1,2,3,2,1, ex: 1,2,3,3,2,1 1,2,3,4,2,1 n'est pas un palindrome

def sum(l: list[float]) -> float:
    sum = 0
    for value in l:
        sum += value
    return sum

def average(l: list[float]) -> float:
    return sum(l) / len(l)

def min(l : list[float]) -> float:
    min = l[0]
    for value in l[1:]:
        if value < min:
            min = value
    return min

def max(l : list[float]) -> float:
    l.sort()
    return l[-1]

def sum_even(l: list[float]) -> float:
    sum = 0 # toto
    for value in l:
        if value % 2 == 0:
            sum += value
    return sum

def palindrome(l: list[float]) -> bool:
    l2 = l.copy().reverse()
    return l2 == l

def palindrome2(l: list) -> bool:
    for i in range(len(l) // 2):
        if l[i] != l[-(i+1)]:
            return False
    return True

if __name__ == '__main__':
    l1 = [1.0,2,3,4,5,6,7,8,9,10]
    print(sum(l1))
    print(average(l1))
    print(min(l1))
    print(sum_even(l1))
    print(palindrome2([1,2,3,2,1]))