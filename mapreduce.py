import time

l = range(100)
print(l)

def infinite_sequence():
    i = 0
    while True:
        yield i
        i+=1
        time.sleep(0.1)

def filter(fn, iterator):
    for val in iterator:
        if fn(val):
            yield val

def map(fn, iterator):
    for val in iterator:
        yield fn(val)

def range(nb):
    i = 0
    while i < nb:
        yield i
        i+=1

def list(iterator):
    res = []
    for val in iterator:
        res.append(val)
    return res

res = filter(lambda x : x % 2 == 0, l)
res = map(lambda x : x ** 2, res)
#res = list(res)
print(res)
#print(len(res))
for val in res:
    print(val)
for val in res:
    print(val)

# Intention List or Comprehension List
res = [x ** 2 for x in l if x % 2 == 0]
print(res)

# Generator
res = (x ** 2 for x in l if x % 2 == 0)
res = list(res)
print(res)

# with open("data/house.csv") as f:
#     for row in f:
#         print(row)



