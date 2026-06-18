try:
    age = input("Age : ")
    age = int(age)
except ValueError as ex:
    print(f"Erreur valeur : {ex}")
except TypeError as ex:
    print(f"Erreur type : {ex}")
except Exception as ex:
    print(f"Unknow error : {ex}")


