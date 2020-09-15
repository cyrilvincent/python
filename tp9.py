v = [220,221,222,223,224.5]
a = [10,11,12,8,9]

print(list(zip(v, a)))

res = [t[0] * t[1] for t in zip(v, a)]
print(res)