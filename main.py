import hello
import toto.mymodule
print(hello.is_prime(7))

from hello import is_prime

def is_prime(x):
    return 0



is_prime()