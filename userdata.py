import json

with open('userdata.json') as f:
    data = json.load(f)


def addSavedBook(username, book):
    data[username]['savedBooks'].append(book)
    with open('userdata.json', 'w') as f:
        json.dump(data, f)


def getSavedBook(username):
    return data[username]['savedBooks']


def addDislikedBook(username, book):
    data[username]['dislikedBooks'].append(book)
    with open('userdata.json', 'w') as f:
        json.dump(data, f)


def getDislikedBook(username):
    return data[username]['dislikedBooks']


def addLikedBook(username, book):
    data[username]['likedBooks'].append(book)
    with open('userdata.json', 'w') as f:
        json.dump(data, f)


def getLikedBook(username):
    return data[username]['likedBooks']


def addTag(username, key, value):
    data[username]['tagRanks'][key] = value


def getTag(username):
    return data[username]['tagRanks']
