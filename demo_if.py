age = 19
genre = 1
# condition = age >= 18
if age >= 18:
    print("Adulte")
    if genre == 1:
        print("Homme")
    else:
        print("Femme")
elif age >= 12:
    print("Ado")
elif age < 2:
    print("BB")
else:
    print("Enfant")