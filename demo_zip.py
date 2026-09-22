ampere = [1,2,1.1,3,5]
volt = [220,221,222,223,224]
for a,v in zip(ampere, volt):
    print(a * v, end=",")

print([a * v for a, v in zip(ampere, volt)])
print([(a, v) for a, v in zip(ampere, volt)])
dicos : list[dict[str, int]] = [{"a":a, "v": v} for a, v in zip(ampere, volt)]
print(dicos[1]["a"])