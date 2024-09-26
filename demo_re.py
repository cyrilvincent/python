import re

s = "aaa toto bbb zeebg$"

regex = r"zee[bg]{2}\$$"

# if re.search(regex, s):
#     print("OK")
# else:
#     print("No match")

tel = "06 22 53 87 62"
regex = r"^(\d{2}[ -]?){5}$"
if re.search(regex, tel):
    print("OK")
else:
    print("No match")

# Saisir un isbn et vérifier s'il est correct
