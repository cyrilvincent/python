vlist = [220, 220, 221, 222]
alist = [10, 10, 11, 12]

res = (a * v for (a, v) in zip(vlist, alist))
print(list(res))
