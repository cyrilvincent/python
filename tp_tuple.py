def min_max_mean(list: list[float]) -> tuple[float, float, float]:
    sum = 0
    min = list[0]
    max = list[0]
    for value in list:
        sum += value
        if value < min:
            min = value
        elif value > max:
            max = value
    return min, max, sum / len(list)

if __name__ == '__main__':
    min, max, mean = min_max_mean([0,1,2,3,4,5,6,7,8,9])
    print(min, max, mean)