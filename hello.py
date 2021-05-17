print("Hello World!")
x = 1
y = 2
print(x + y)

x = x + 1 # x = 2
x += 1 # 3

print(5 / 2) # 2.5
print(5 // 2) # 2
print(5 % 2) # 1

print("toto\ntiti")
print(r"toto\ntiti")
print(r"c:\path")
print("c:\toto")

age = 12
birth_date = 1972
print(type(birth_date))
s = "toto"
print(type(s))
s = "123"
x = 123
y = 3.14
print(x + y)
s2 = "456"
print(s + s2)

a = 2
b = 3
a, b = b, a

age = input("Entrez votre age: ")
age_integer = float(age) # int); float(); str()
print(1 + age_integer)
s = "toto"
print(s.upper())
print(s + " " + str(age_integer))
print(f"{s} a {age_integer:.0f} ans")