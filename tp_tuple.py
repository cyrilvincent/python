def avg_min_max(l: list[int]) -> tuple[float, int, int]:
    sum = 0
    min = l[0]
    max = l[0]
    for value in l:
        sum += value
        if value < min:
            min = value
        elif value > max:
            max = value
    return sum / len(l), min, max


if __name__ == '__main__':
    l = list(range(100))
    avg, min, max = avg_min_max(l)
    print(avg, min, max)
    assert 49.5 == avg
    assert 0 == min
    assert 99 == max

