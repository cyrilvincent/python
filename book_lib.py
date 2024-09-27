import json

def load(path: str):
    with open(path, "r") as f:
        res = json.load(f)
    return res

if __name__ == '__main__':
    res = load("data/media/books.json")
    print(res[1]["title"])