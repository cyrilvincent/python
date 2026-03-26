while True:
    try:
        largeur = int(input("Largeur: "))
        longueur = int(input("Longueur: "))
        if longueur < 0 or largeur < 0:
            raise ValueError("Longueur ou largeur < 0")
        if longueur < largeur:
            raise ValueError("Longueur < largeur")
        surface = longueur * largeur
        print(surface)
        break
    except ValueError as ex:
        print(f"Erreur de type {ex}")

# Tp reprendre le tp 1 et gérer les erreurs tant qu'il y a des erreurs
# Lever une erreur dans facto() si n < 0
