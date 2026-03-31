while True:
    try:
        age = int(input("Age: "))
        if age < 0:
            raise ValueError("Age < 0")
        print(age + 1)
        break
    except ValueError as ex:
        print(f"Erreur: {ex}")
print("OK")