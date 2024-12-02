# i = 0
# while i < 10:
#     print(i)
#     i += 1

start = 10
end = -1
step = -2
for i in range(start, end, step):
    print(i)

total = 0
for i in range(100):
    if i > 50:
        break
    total += i
print(total)