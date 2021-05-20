import re

pattern = "a(bc)+"
value = "abcbcbcbcbcbc"

if re.match(pattern, value):
    print("OK")
else:
    print("KO")