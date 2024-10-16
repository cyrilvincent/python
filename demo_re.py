import re

s = "xaxbxcxbxax"
regex = (r"^(x\w)+x$")


if re.search(regex, s):
    print("Match")
else:
    print("No match")

chaine = ""
regex = r"^\d{3}[- ]?\d[- ]?\d{4}[- ]?\d{4}[- ]?\d$"
while re.search(regex, chaine) is None:
    chaine = input("Saisir un EAN-13 valide: ")
print(chaine)