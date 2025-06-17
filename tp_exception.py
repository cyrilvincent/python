while True:
    try:
        age_string = input("Age: ")
        age = int(age_string)
        print(age)
        break
    except ValueError as ex:
        print(f"Erreur: {ex}")
