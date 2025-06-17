while True:
    try:
        age_string = input("Age: ")
        age = int(age_string)
        if age < 0 or age > 120:
            raise ValueError("Age incohérent")
        print(age)
        break
    except ValueError as ex:
        print(f"Erreur: {ex}")
