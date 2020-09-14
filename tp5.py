l = [1,2,5,99,-8,54,53,6,7,98]

def filter_even(l):
    res = []
    for val in l:
        if val % 2 == 0:
            res.append(val)
    return res

print(filter_even(l))
