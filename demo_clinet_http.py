import urllib.request

with urllib.request.urlopen("http://132.168.57.253:5000/dict") as res:
    print(res.read())
