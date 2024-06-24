def add(a:float, b=0.) -> float:
    return a + b


c = add("toto",2)
print(c)

c = add(a=3, b=2)
print(c)

c = add(2)
add()

c = add(b=3)

add("toto", 3)
