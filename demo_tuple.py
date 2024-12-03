def toto():
    return 1,2,3

x, y, z = toto()
print(x ,y, z)

# def min_max_average(l): 1 seule iteration sum/len
# return tuple des 3 float
# test
def min_max_average(l):
    min = l[0]
    max = l[0]
    sum = 0
    for value in l:
        sum += value
        if value < min:
            min = value
        elif value > max:
            max = value
    return min, max, sum / len(l)

if __name__ == '__main__':
    print(min_max_average(range(100)))