import json

with open('bookStorage.json') as f:
    data = json.load(f)

def add(isbn,book):
    data[isbn] = book;
    with open('bookStorage.json', 'w') as f:
        json.dump(data, f)

def get(isbn):
    return data[isbn]


