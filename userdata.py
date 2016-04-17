import json, time

#Entry format for SavedBook, LikedBook, DislikedBook lists:
#[[isbn, date], [isbn2, date2], ...]
#So an array of subarrays, where each subarray contains an isbn identifier, and the date it was added to this list

with open('userdata.json') as f:
    data = json.load(f)

def addSavedBook(username, isbn):
    entry = [isbn, time.strftime("%x")]
    data[username]['savedBooks'].append(entry)
    with open('userdata.json', 'w') as f:
        json.dump(data, f)


def getSavedBookList(username):
    return data[username]['savedBooks']


def addDislikedBook(username, isbn):
    entry = [isbn, time.strftime("%x")]
    data[username]['dislikedBooks'].append(entry)
    with open('userdata.json', 'w') as f:
        json.dump(data, f)


def getDislikedBookList(username):
    return data[username]['dislikedBooks']


def addLikedBook(username, isbn):
    entry = [isbn, time.strftime("%x")]
    data[username]['likedBooks'].append(entry)
    with open('userdata.json', 'w') as f:
        json.dump(data, f)


def getLikedBookList(username):
    return data[username]['likedBooks']


def addTag(username, key, value):
    data[username]['tagRanks'][key] = value


def getTagList(username):
    return data[username]['tagRanks']
