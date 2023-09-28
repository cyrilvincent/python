import re

# regex = r"a(bc)*d[ez]?f"
# regex = r"[\w.-_\d]+@[\w.-_\d]+.\w+"
regex = r"^\d{3}-\d-\d{4}-\d{4}-\d$"

while True:
    s = input("Saisir le mot à vérifier: ")
    if re.match(regex, s):
        print("OK")
        break
    else:
        print("KO")