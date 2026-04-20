age = 17
wind_speed = 20

if age < 18 and wind_speed == 20:
    print("Mineur et peu de vent")
else:
    print("Majeur")

condition = age < 18 or wind_speed == 20
if condition:
    print("Mineur et peu de vent")