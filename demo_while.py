# i = 0
# while i < 100:
#     print(i)
    # i -= 1 # <=> i = i + 1

i = 0
while i <= 10:
    j = 0
    while j <= 10:
        print(f"{i}*{j}={i*j}")
        j += 1
    i += 1

i = 0
while i < 100:
    if i % 2 == 0:
        print(i * 2)
    else:
        print(i - 1)
    i += 1