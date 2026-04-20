# i = 0
# while i < 10:
#     print(i)
#     i += 2
#     # i = i + 2
#
# i = 0
# while i < 10:
#     if i%2 == 0:
#         print(i * 2)
#     else:
#         print(i / 2)
#     i += 1

i = 0
j = 0
while i <= 10:
    while j <= 10:
        print(f"{i}+{j}={i + j}")
        j += 1
    j = 0
    i += 1