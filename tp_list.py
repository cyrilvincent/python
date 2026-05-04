# l = [1,2,3,55,99,-2,4,8,-3,1000]
# for v in l:
#     print(v)
#
# for i in range(len(l)):
#     print(l[i])
#
# for i, v in enumerate(l):
#     print(i, v, l[i])

def sum(l: list[float]) -> float:
    total = 0
    for v in l:
        total += v
    return total

def filter_even(l: list[int]) -> list[int]:
    pass