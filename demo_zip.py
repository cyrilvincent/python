volts = [220, 221, 220, 222, 222.5]
amps = [10, 11, 10.5, 10, 10.2]
powers = []

for v, a in zip(volts, amps):
    p = v * a
    powers.append(p)

print(powers)
