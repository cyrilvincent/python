# for i in range(10):  # 1 seul paramètre : start = 0, end = 10-1
#     print(i)

# for i in range(6, 10): # 2 paramètres : start = 6, end = 10-1
#     print(i)

for i in range(2, 10, 2):  # 3 paramètres : start = 2, end = 10-1, step = 2
    print(i)

start = 1
stop = 11
step = 2
for i in range(start, stop, step):
    print(i)

for i in range(10, 0, -1):
    if i == 5:
        continue
    print(i)
