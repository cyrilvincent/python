import re

regex = "^\d-\d{4}-\d{4}-\d$"
phone = "2-7654-1005-4"
if re.match(regex, phone):
    print("OK")
else:
    print("KO")