import re

def is_ean(ean: str) -> bool:
    regex = r"^\d(\s\d{6}){2}$"
    if re.search(regex, ean):
        return True
    else:
        return False

def is_mail(mail: str) -> bool:
    regex = r"^\w[\w\d_-]*@[\w\d_-]+.\w{2,6}$"
    if re.search(regex, mail):
        return True
    else:
        return False


if __name__ == '__main__':
    ean="1 123456 123456"
    res = is_ean(ean)
    print(res)
    ean = "1 123456 12345"
    res = is_ean(ean)
    print(res)
    mail = "contact@cyrilvincent.com"
    res = is_mail(mail)
    print(res)
