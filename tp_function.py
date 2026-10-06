# Faire la fonction multiply qui multiplie 2 ou 3 nb
# Documenter
# Faire la fonction factorielle(n)
# Faire la fonction fibonacci(n)

def multiply(a: float, b: float, c: float = 1.0) -> float:
    """
    Multplie les nb
    :param a:
    :param b:
    :param c: facultatif 1 par défaut
    :return: a * b * c
    """
    return a * b * c + 1

def factorielle(n: int) -> int:
    facto = 1
    for i in range(2, n + 1):
        facto = facto * i
    return facto

if __name__ == '__main__':  #main+tab
    assert multiply(2,3) == 6
    assert factorielle(5) == 120

# Dans tp_fonction regrouper tous les tests en fin de fichier
# Mettre un main+tab
# Bonus: mettre des assert
# Créer un main.py qui importe tp_fonction et appel les fonctions avec des input
