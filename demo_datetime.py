import datetime

dt1 = datetime.datetime.now()
print(dt1)
dt2 = datetime.datetime(2024,12,5,14,34)
print(dt2)
print(dt1 - dt2)
print(dt1.isoformat())
print(dt1.strftime("%d/%m/%Y"))
dt3 = datetime.datetime.strptime("06/12/2024", "%d/%m/%Y")
print(dt3)