# Créer la variable x = 1
# Incrémenter x de 2
# Afficher x
# Créer la variable s = "hello world"
# Afficher le w de s
# Créer la variable year = 2023
# Saisir votre année de naissance
# Afficher votre age
# tester le debugger + point d'arrêt

x = 1
x += 2
print(x)

s = "Hello World!"
print(s[6])

year = 2023
birth = input("Année de naissance: ")
birth_int = int(birth)

age = year - birth_int
print(f"Vous avez {age} ans")

if age > 18:
    print("Adulte")
    print("Toto")

print("Titi")



