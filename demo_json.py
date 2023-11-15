import json

with open("data/media/books.json") as f:
    books = json.load(f)

print(books[0]["title"])