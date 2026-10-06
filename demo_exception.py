while True:
    q =input("Saisir un nb: ")
    try:
        q = int(q)
        print( 1 / q)
        break
    except ValueError as ve:
        print(f"Erreur lié à la valeur: {ve}")
    except ZeroDivisionError as zde:
        print(f"Ne peut pas être zéro: {zde}")
