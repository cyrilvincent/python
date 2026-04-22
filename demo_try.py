while True:
    try:
        x = input("Saisir x < 10: ")
        x = int(x)
        if x >= 10:
            raise ValueError("Valeur interdite")
        result = 1 / x
        print(result)
        break
    except ZeroDivisionError as ex:
        print(f"Division par zéro: {ex}")
    except ValueError as ex:
        print(f"Erreur sur la valeur: {ex}")