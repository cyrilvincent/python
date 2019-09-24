for i in range(10,-1,-1):
    print(i)

nb = int(input("Number:"))

isPrime = True

if nb < 2:
    isPrime = False
for div in range(2,int((nb ** 0.5)) + 1):
    if nb % div == 0:
        isPrime = False
        break

print(f"{nb} is prime: {isPrime}")

