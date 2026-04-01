tensions = [220,220,221,222,223]
courants = [1,1.1,1.2,1.3,1.1]

for t, a in zip(tensions, courant):
    power = t * a
    print(power)
