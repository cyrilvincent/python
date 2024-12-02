import sys

print("Hello World")
print(sys.version)

a = 1
b = 2
a = a + 1
# <=>
a += 1
print(a, b, a+b, a%2)

text = "Ma chaîne \"\n\t\\de caractères"
text2 = """gdfgdrgdrgrd
drgredger"gre
rgerqgeqrger
gergergeqrg"""
print(text2)

temperature_room_a148 = 23.7
print(temperature_room_a148)

a = 1
b = 3.14
print(type(a), type(b))
c = a + b
print(float(c))
print(len(text2))
text = input("Saisir du nombre:")
value = int(text)
print(value + 1)

text = "toto"


