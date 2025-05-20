

# Resaisir l'age indefiniment tant que ce n'est pas un entier
# Tips: while True + break
# Idem pour les ages < 0 : raise

while True:
    try:
        age = input("Age: ")
        age = int(age)
        if age < 0:
            raise ValueError("Age négatif")
        print(age)
        break
    except ValueError as error:
        print(f"Erreur sur l'age : {error}")