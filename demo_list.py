l1 = [9,8,55,4,99,-2,5,99]

l1.append(100)
print(l1)
sum = 0
for value in l1:
    sum = sum + value

print(sum / len(l1))


def sum(l: list[float]) -> float:
    sum = 0
    for value in l:
        sum += value
    return sum

# for i in range(len(l1)):
#     print(l1[i])