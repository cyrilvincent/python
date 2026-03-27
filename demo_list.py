l1 = [10,8,77,5,-2,58,99]
# print(l1)
# for value in l1:
#     print(value)
# print(l1[2])
# print(l1[-1])
# print(l1[1:6])
# print(l1[1:-1])
# print(l1[2:-2])
# index = l1.index(58)
# print(index)
# l1.append(999)
# print(l1)
# l1.remove(99)
# print(l1)
# l1[1]=888
# print(l1)

for i in range(len(l1)):
    print(l1[i])



def sum(l: list[float]) -> float:
    """
    sum
    :param l: blah blah
    :return:
    """
    total = 0
    for value in l:
        total += value
    return total

def clone(l: list[float]) -> list[float]:
    new_list = []
    for value in l:
        new_list.append(value)
    return new_list

def double(l: list[float]) -> list[float]:
    new_list = []
    for value in l:
        new_list.append(value * 2)
    return new_list


if __name__ == '__main__':
    assert sum([1,2,3]) == 6
    assert sum([]) == 0
    assert clone([1,2,3]) == [1,2,3]
    assert double([1,2,3]) == [2,4,6]
