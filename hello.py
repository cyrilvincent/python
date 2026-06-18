import sys

print("he\n\\llo\u2048")
print(sys.version)

a = 1
a = a + 1
a += 1
b = "toto"
c = "2"
d = 3.16
print(a + d)
print(len(b))

print(type(a), type(b))


# x = input("Saisir x:")
# x = int(x)
# print(x + 1)
b = b.upper()
print(b)

print(f"La valeur de a est {a:02d}")

my_bool = True
if my_bool:
    print("True")


a = 1
b = 2

condition = (a <= 1) or ((b + a) >= 2)
if condition:
    print("OK")

for i in range(10, 5, -2):
    print(i)

for i in range(10):
    if i == 5:
        continue
    print(i)