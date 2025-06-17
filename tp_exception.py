try:
    age_string = input("Age: ")
    age = int(age_string)
    print(age)
except ValueError as ex:
    print(f"Erreur: {ex}")
