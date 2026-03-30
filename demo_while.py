i = 10
j = 5
while i >= 0 and j < 10:
    if i == 0:
        print("BOOOOOM")
    else:
        print(i)
    i -= 1

x = 0
y = 0
while x <= 10:
    y = 0
    while y <= 10:
        print(f"{x}*{y}={x*y}")
        y += 1
    x += 1