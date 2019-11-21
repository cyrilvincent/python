import tp2
import math

l = [1,-1,0,2,5,99,-50,22,25,27]

def filterByFn(l, fn):
    res = []
    for i in l:
        if fn(i):
            res.append(i)
    return res

def mapByFn(l, fn):
    res = []
    for i in l:
        res.append(fn(i))
    return res


if __name__ == '__main__':
    # print(filterByFn(l, lambda x : x % 2 == 0))
    # res = filter(lambda x: x % 2 == 0, l)
    # for i in res:
    #     print(i)
    #
    # print(mapByFn(l, lambda x : math.sin(x * 2)))
    # res = map(lambda x : x + 1, l)
    # for i in res:
    #     print(i)

    # l = range(10000000000000000000000000000000)
    # res = filterByFn(l, lambda x : tp2.isPrime(x))
    # res = mapByFn(res, lambda x : x ** 2)
    # res = filterByFn(res, lambda x : x % 2 == 0)
    # for i in res:
    #     print(i)

    # l = range(10000000000000000000000000000000)
    # res = filter(lambda x : tp2.isPrime(x), l)
    # res = map(lambda x : x ** 2, res)
    # res = filter(lambda x : x % 2 == 0, res)
    # print(len(res))
    # for i in res:
    #     print(i)

    l = range(10)
    res = map(lambda x : x ** 2, filter(lambda x : x % 2 ==0, l))
    #<=>
    res = [x ** 2 for x in l if x % 2 == 0]

    l1 = [1,2,3,4,5,6,7,8,9,10]
    l2 = [1,3,3,4,5,6,8,8,7,10]
    res = list(zip(l1, l2))
    print(res)
    res = [(t[0]-t[1]) ** 2 for t in res if (t[0]-t[1]) != 0]
    res = [(x - y) ** 2 for x,y in res if (x - y) != 0]
    res = map(lambda t : (t[0]-t[1]) ** 2, filter(lambda t : (t[0]-t[1]) != 0, res))

