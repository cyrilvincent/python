import sys

print("Hello")
i = 1
print(i)
i = "toto"
print(type(i))
# s = input("Hello:")
# print(int(s) + 1)
print(sys.version)

for i in range(20, 10, -2):
    print(i)


def add(i: float, j: float=0, k: float=0) -> float:
    return i + j + k


res = add(1,3)
res = add(1,k=3)

res = add(i=1, k=3)
print(res)


def toto(*kargs):
    for value in kargs:
        print(value)

def titi(**kwargs):
    for key in kwargs.keys():
        print(key)

def tutu(a,*kargs,**kwargs):
    pass




toto()
toto(1)
toto(1, 2, 3, 4)

titi(a=1,b=2,tutu=3)

f = add

def invoke(a,b,fn):
    return fn(a,b)



print(invoke(1,2,lambda x,y: x + y))