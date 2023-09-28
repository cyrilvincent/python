import re

regex = r"a(bc)*d[ez]?f"
regex = r"[\w.-_\d]+@[\w.-_\d]+.\w+"

while True:
    s = input("Sasir le mot à vérifier: ")
    if re.match(regex, s):
        print("OK")
    else:
        print("KO")