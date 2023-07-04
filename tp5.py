# Import tp4
# Saisir un entier
# Exception si non entier
# Appeler tp4.is_prime
# Si nb < 0 lever l'exception ValueError dans is_prime
# Traiter l'exception nb < 0
import tp4

stop = False
while not stop:
    try:
        nb = int(input("Saisir nb: "))
        print(tp4.is_prime(nb))
        stop = True
    except ValueError:
        print("nb n'est pas un entier")
    except TypeError as ex:
        print(ex)