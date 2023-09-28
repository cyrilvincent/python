try:
    s = input("Saisir une année: ")
    year = int(s)
    print(year)
    print(1 / year)
# except Exception as ex:
#     print(type(ex))
except ValueError:
    print("Erreur")
except ZeroDivisionError:
    print("Division erreur")
