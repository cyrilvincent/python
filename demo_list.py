def sum(l: list[float]) -> float:
    total=0
    for i in l:
        total+=i
    return total

def sum2(l: list[float]) -> float:
    total=0
    for i in range(len(l)):
        total+=l[i]
    return total

if __name__ == '__main__':
    l = [1, 99, 50, -1, 23, 45, 7, 11, 9, 10]
    print(l[2:8])
    l.append(999)
    print(l)
    l.insert(5, -10)
    print(l)
    l.remove(23)
    print(l)
    l[2] = 51
    print(l)
    if 99 in l:
        print("99 est présent")
    for i in l:
        print(i)
    print(sum2(l))
