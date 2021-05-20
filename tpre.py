import re

# Saisir un ISBN13
# 978-2-7654-0912-0
# Afficher Ok ou ko
# Répéter la saisie tant que KO

pattern = r"^\d{3}-\d-\d{4}-\d{4}-\d$"
value = ""
while True:
    value = input("Saisir un ISBN: ")
    if re.match(pattern, value) is None:
        print("KO")
    else:
        print("OK")
        break

