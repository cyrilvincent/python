# Saisir un entier et afficher s'il est pair ou impair
# Saisir votre age et afficher votre catégorie d'age
# < 1 : bb
# 12 : enfant
# 18 : ado
# > 18 : adulte
# 64 : retraité
# 80 : grand age

# i = int(input("Entier: "))
# if i % 2 == 0:
#     print("Pair")
# else:
#     print("Impair")


age = int(input("Age: "))
if age < 1:
    print("BB")
elif age < 12:
    print("Enfant")
elif age < 18:
    print("Ado")
else:
    print("Adulte")
    if age > 64:
        print("Retraité")
        if age > 80:
            print("Grand age")
