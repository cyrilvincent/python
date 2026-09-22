# Créer une liste l avec 10 éléments non consécutifs "en dur" l = [1,2,3,8,9,-1,99,0,66]
# Créer la fonction display(l: list[int]) => print
# Créer la fonction sum(l) -> int
# Créer la fonction max(l)
# Créer la fonction filter_even(l) -> list[int] : [1,2,3,4] => [2,4]
# Créer la fonction filter_prime(l) : [1,2,3,4,5] => [2,3,5]
import tp_function

def display(l: list[int]):
    for v in l:
        print(v)

def sum(l: list[int]) -> int:
    total = 0
    for v in l:
        total += v
    return total

def max(l: list[int]) -> int:
    max = l[0]
    for v in l[1:]:
        if v > max:
            max = v
    return max

def filter_even(l: list[int]) -> list[int]:
    result = []
    for v in l:
        if v % 2 == 0:
            result.append(v)
    return result

def filter_prime(l: list[int]) -> list[int]:
    result = []
    for v in l:
        if tp_function.is_prime(v):
            result.append(v)
    return result


if __name__ == '__main__':
    l = [1, 2, 3, 8, 9, -1, 99, 0, 66, 88]
    display(l)
    assert sum(l) == 275
    assert max(l) == 99
    assert filter_even(l) == [2,8,0,66,88]
    assert filter_prime(l) == [2,3]
