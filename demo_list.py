l = [1,5,6,8,9,0,-1,7]
# l.append(99)
# l.insert(2,88)
# print(l)
#
# for value in l:
#     print(value)
#
# for i in range(len(l)):
#     print(l[i])


def hello(l: list[float]):
    for val in l:
        print(val)

# 3.14 != [3.14]


# TP
# Créer la fonction sum(l:list[float]) -> float
# Créer la fonction max(l:list[float]) -> float, idem pour min
# Créer la fonction average
# Bonus : créer la fonction filter_even(l:List[float]) -> list[float]
# filter_even([1,2,3,4]) -> [2,4]

def sum(l: list[float]) -> float:
    total = 0
    for value in l:
        total += value
    return total


def max(l: list[float]) -> float:
    max = l[0]
    for value in l[1:]:
        if value > max:
            max = value
    return max

def average(l: list[float]) -> float:
    return sum(l) / len(l)

def filter_even(l: list[float]) -> list[float]:
    res = []
    for value in l:
        if value % 2 == 0:
            res.append(value)
    return res

print(sum(l))
print(max(l))
print(average(l))
print(filter_even(range(100)))
print(filter_even([1,2,3,4]))
