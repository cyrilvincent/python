# i = 10
# j = 0
# while i > 0 or j < 100:
#     if i % 2 == 0:
#         print(i)
#     i -= 1
#     j += 2

start = 100
end = 1
step = -2
total = 0
for i in range(start, end,step):
    total += i
print(total)