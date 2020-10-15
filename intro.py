print("Hello World")
# function = ()
print(3/2) # 1.5
print(3//2) # 1
print(3 % 2) # 1
f = 3.14 # 64 bits
b = 1 == 2
print(type(b))
print(type(f))
l1 = [1,2,3]
l2 = [1,2,3]
print(l1 == l2)
print(l1 is l2)
print(type(b) is bool)
print(2 != 3)

mémé = "téré"
s = "unicode"
s = b"tete"
print(s)
print(type(s))
utf = s.decode("UTF-8")
latin1 = utf.encode("iso_8859_1")

with open("data/house.csv","r") as f:
    s = f.read()
    with open("data/house-binary.csv","wb") as f2:
        f2.write(s.encode("ISO-8859-1"))

with open("data/house-binary.csv","r",encoding="ISO-8859-1") as f:
    s = f.read().encode("utf8")

with open("data/house-binary.csv","rb") as f:
    s = f.read().decode("UTF-8")

with open("data/neige.jpg","rb") as f:
    bytes = f.read()

