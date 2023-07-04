# Faire la fonction sum(l) -> float
# Faire average(l)
# Faire les fonctions min, max

def sum(l) -> float:
    sum = 0
    for val in l:
        sum += val
    return sum

def average(l) -> float:
    return sum(l) / len(l)

def min(l) -> float:
    min = l[0]
    for val in l[1:]:
        if val < min:
            min = val
    return min

def max(l) -> float:
    max = l[0]
    for val in l[1:]:
        if val > max:
            max = val
    return max

if __name__ == '__main__':
    l1 = [1,2,3,4,5,6,7,8,9,10]
    print(sum(l1))
    print(average(l1))
    print(min(l1))
    print(max(l1))