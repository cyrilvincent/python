

def move(point: tuple[float, float], x: float, y: float) -> tuple[float, float]:
    return (point[0]+x, point[1]+y)

def stats(l: list[float]) -> tuple[float, float]:
    return 0,1

if __name__ == '__main__':
    point = (3, 2)
    point = move(point,1,-1)
    print(point)
    min, max = stats([1,2,3])
    print(min, max)