l = [1,2,3,4,5,6,7,8,9,0]
for v in l:
    print(v)

print(len(l))

def sum(l: list[float]) -> float:
    sum = 0
    for v in l:
        sum += v
    return sum

print(sum([1.,2,3]))
