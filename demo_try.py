while True:
    try:
        age = int(input("age: "))
        print(age)
        break
    except ValueError as ex:
        print(f"Erreur: {ex}")