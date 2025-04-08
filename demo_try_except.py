while True:
    try:
        age = int(input("Saisir age: "))
        break
    except ValueError as ex:
        print(f"Error: {ex}")
    except TypeError:
        print("Type error")
print(age)
