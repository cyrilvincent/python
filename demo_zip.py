tensions = [220,221,222,221,220,219]
courants = [10.0,10.1,9.9,10,11,10.5]

res = [tension * courant for tension, courant in zip(tensions, courants)]
print(res)