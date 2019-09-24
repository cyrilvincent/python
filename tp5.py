# Refaire TP1 avec gestion des erreurs et resaisie de l'age en cas d'erreur

isCorrect = False
s = ""
while not isCorrect:
    try:
        year = 2019
        s = input("Birth date:")
        birth = int(s)
        isCorrect = True
        age = year - birth
        print(f"Your age is {age}")
    except ValueError:
        print(f"{s} is not an integer")