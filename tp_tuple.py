# Ecrire la fonction min_max_avg(l: list[int]) -> tuple[int, int, float] en une seule itération

def min_max_avg(l : list[int]) -> tuple[int, int, float]:
    min = l[0]
    max = l[0]
    total = 0
    for v in l:
        total += v
        if v < min:
            min = v
        elif v > max:
            max = v
    return min, max, total / len(l)

if __name__ == '__main__':
    l = list(range(10))
    min, max, avg = min_max_avg(l)
    print(min, max, avg)
    assert min_max_avg(l) == (0,9,4.5)