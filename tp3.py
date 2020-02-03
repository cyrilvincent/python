year = input("Saisir une année: ")
try:
    year = int(year)
    print(1 / year)
except ValueError as ex:
    print(f"Error {ex}")
except TypeError as ex:
    print(f"Error {ex}")
except ZeroDivisionError as ex:
    print(f"Zero Division {ex}")