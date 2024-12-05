import re

regex = "^0[1-7]|9-\d{2}-\d{2}-\d{2}-\d{2}$"
phone = "06-22-53-87-62"
if re.match(regex, phone):
    print("OK")
else:
    print("KO")