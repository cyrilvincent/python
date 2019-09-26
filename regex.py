import re

s = "contact@cyrilvincent.com"

if re.search(r"^contact@cyril(a[bze]c)?vinc?ent.com$", s) is not None:
    print("OK")


res = re.sub(r"(cyril)(vincent)",r"\1-\2",s)
print(res)

regex = r"^\d{3}-\d-\d{3}-\d{5}-\d$"
isbn = "978-2-409-00217-5"
print(re.search(regex, isbn))



