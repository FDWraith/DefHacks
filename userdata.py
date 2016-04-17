import json, time, main

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
    with open('userdata.json', 'w') as f:
        json.dump(data, f)

def getTagDict(username):
    return data[username]['tagRanks']

#returns a tag over the threshold, else returns None
def getPopularTag(username):
    maxPop = 0
    popTag = None
    #NOT BEING USED
    popTagType = ''
    rankedTags = data['username']['tagRanks']
    for key in rankedTags:
        if rankedTags[key][0] > 3 and rankedTags[key][0] > maxPop:
            maxPop = rankedTags[key]
            popTag = key
    return popTag


def getCurrentBook(username):
    retBook = book.Book()
    retBook.fillFromJSON(data[username]['currentBook'])
    return retBook;


def changeCurrentBook(username, book):
    data[username]['currentBook'] = book.getAsJSON();
    with open('userdata.json', 'w') as f:
        json.dump(data, f)

def getNum(username):
    return data[username]['num']


def changeNum(username, offset):
    data[username]['num'] = data[username]['num'] + offset
    with open('userdata.json', 'w') as f:
        json.dump(data, f)


def getP(username):
    return data[username]["P"]


def setP(username, newP):
    data[username]["P"] = newP
    with open('userdata.json', 'w') as f:
        json.dump(data, f)
