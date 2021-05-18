import tp4
import math

# def filter_multiple(l, multiple):
#     res = []
#     for value in l:
#         if value % multiple == 0:
#             res.append(value)
#     return res
#
# def filter_prime_number(l):
#     res = []
#     for value in l:
#         if tp4.is_prime(value):
#             res.append(value)
#     return res

def my_filter(fn, l):
    res = []
    for value in l:
        if fn(value):
            res.append(value)
    return res

def my_map(fn, l):
    res = []
    for value in l:
        res.append(fn(value))
    return res


if __name__ == '__main__':
    l1 = [1, 9, 3, 4, 3, 10, 17, 8, 2, 0]
    # print(filter_multiple(l1, 2))
    # print(filter_multiple(l1, 3))
    # print(filter_prime_number(l1))
    print(list(filter(tp4.is_even, l1)))
    print(list(filter(lambda x: x % 2 == 0, l1)))
    print(list(filter(tp4.is_prime, l1)))
    print(list(filter(lambda x: tp4.is_prime(x), l1)))
    l2 = filter(lambda x: tp4.is_prime(x), l1)
    print(list(map(lambda x: x + 1, l2)))
