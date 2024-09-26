# Lire data/media/books.json
# Afficher la liste
# Afficher le nombre de livre
# Afficher le titre du 1er livre
# Afficher le prix du 2ème livre
# Afficher l'id du dernier livre
# Bonus : Afficher la liste des prix

import json

with open("data/media/books.json", "r") as f:
    books = json.load(f)

print(books)
print(len(books))
print(books[0]["title"])
print(books[1]["price"])
print(books[-1]["id"])
prices = [float(b["price"]) for b in books]
print(prices)