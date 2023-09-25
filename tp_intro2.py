x1 = float(input("X1: "))
y1 = float(input("Y1: "))
x2 = float(input("X2: "))
y2 = float(input("Y2: "))

distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
print(f"(x1, y1)=({x1:.2f},{y1:.2f})")
print(f"Distance={distance:.2f}")