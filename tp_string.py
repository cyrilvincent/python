# Saisir un mot
# Afficher le nb de lettre du mot
# Afficher le 3ème caractère (index 2)
# Afficher les 3 1er catactères
# Afficher tout sauf le 1er et dernier caractère, par exemple python => ytho

word = input("Word: ")
print(len(word))
print(word[2])
print(word[:3])
n=2
print(word[n:-n])
print(word[-1:0:-1])
