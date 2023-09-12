import math as m
import numpy as np
import my_module
import directory1.subdirectory1.my_module2 as m

def cos(x):
    print("Fake function")

m.cos(0)
np.cos(0)
cos(0)

print(my_module.is_even(8))


