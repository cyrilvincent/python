print("Hello World!")
i = 1
i += 1
print(i)
print(type(i))
s = "toto"
print(type(s))

ok = False
while not ok:
    try:
        year = input("Saisir une année:")
        print(type(year))
        year = int(year)
        ok = True
    except:
        print("Merci de saisir une date")
year += 1
print(f"L'année prochaine sera: {year}")