def move(point: tuple[float, float], x_dep: float, y_dep: float) -> tuple[float, float]:
    return (point[0] + x_dep, point[1] + y_dep)

def get_min_max_avg(l: list[float]) -> tuple[float, float, float]:
    # TP
    return 0, 10, 5

if __name__ == '__main__':
    point1 = (3.0, 2.0, 1.0)
    result = move(point1, 4, -1)
    print(result)
    min, max, avg = get_min_max_avg([1,2,3])
    print(min, max, avg)
