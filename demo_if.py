i = 5
j = 7
k = 8
condition = i % 3 == 0 and (j % 7 == 0 or k < 5)
if condition:
    print(i)
    if i % 5 == 0:
        print("Bingo")
        if i % 99 == 0:
            print("Toto")
print("---")