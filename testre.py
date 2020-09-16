import re

while True:
    x = input("ISBN: ")
    expression = "^\d{3}-\d-\d{4}-\d{4}-\d$"
    if re.search(expression, x) is None:
        print("False")
    else:
        print("True")