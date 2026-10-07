# Créer une liste de 10 éléments
# my_list = [1,2,3,8,99,5,-2,8,1,0]
# Faire la fonction sum(l: list[int]) -> int
# Faire la fonction max(l: list[int]) -> int
# Bonus : faire la fonction filter_even(l: list[int]) -> list[int] : filter_even([1,2,3,4]) -> [2,4]

def sum(l: list[int]) -> int:
    total = 0
    for value in l:
        total += value
    return total

def max(l: list[int]) -> int:
    max = l[0]
    for value in l:
        if value > max:
            max = value
    return max

def filter_even(l: list[int]) -> list[int]:
    result = []
    for value in l:
        if value % 2 == 0:
            result.append(value)
    return result


if __name__ == '__main__':
    my_list = [1,2,3,8,99,5,-2,8,1,0]
    print(sum(my_list))
    assert sum(my_list) == 125
    assert max(my_list) == 99
    assert filter_even(my_list) == [2,8,-2,8,0]

