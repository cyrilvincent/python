a = (1, 2)
print(a[0], a[1])

def toto() -> tuple[float, int]:
    return 1.0, 2

a, b = toto()
print(a, b)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def min_max_avg(l: list[int]) -> tuple[int, int, float]:
    pass

# tester