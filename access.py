#This file is a function
import json, requests

def getOpenLibraryBook(isbn):
    #returns a dictionary of info on the book indicated by the isbn
    url = "https://openlibrary.org/api/books?bibkeys=ISBN:{num}&format=json&jscmd=data".format(num = isbn);
    r = requests.get(url);
    rawData = json.loads(r.text);
    if(rawData == { }):
        return { };
    bookDict = rawData["ISBN:{num}".format(num=isbn)]
    return bookDict

def getNewYorkTimesList(listname,offset):
    url = 'http://api.nytimes.com/svc/books/v2/lists/{name}'.format(name=listname);
    payload = {'api-key': '07dd07bcee660b08c3193b8876620845:13:75015836', 'offset': offset};
    r = requests.get(url,params=payload);
    rawData = json.loads(r.text);
    data = rawData['results'];
    d = [];
    for i in data:
        d.append( { 'title' : i['book_details'][0]['title'],
                    'description' : i['book_details'][0]['description'],
                    'author' : i['book_details'][0]['author'],
                    'isbn' : i['book_details'][0]['primary_isbn10'],
                    'url' : i['book_details'][0]['amazon_product_url']} );
    return d;

def getGoogleBookById(volume_id):
    url = 'https://www.googleapis.com/books/v1/volumes/' + volume_id
    payload = {'key':'AIzaSyAyR0m9gfSIuddjfY6nskanTg08X_62ICM'}
    r = requests.get(url,params=payload)
    rawData = json.loads(r.text)
    return rawData

def getGoogleBookByISBN(book_isbn):
    url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:' + book_isbn
    payload = {'key':'AIzaSyAyR0m9gfSIuddjfY6nskanTg08X_62ICM'}
    r = requests.get(url,params=payload)
    rawData = json.loads(r.text)
    if(rawData == { }):
        return { };
    return rawData

def searchGoogleBooksByCategory(book_cat, offset):
    url = 'https://www.googleapis.com/books/v1/volumes?q=subject:' + book_cat
    url += '&printType=books'
    url += '&startIndex=' + offset
    url += 'maxResults=20'
    payload = {'key':'AIzaSyAyR0m9gfSIuddjfY6nskanTg08X_62ICM'}
    r = requests.get(url,params=payload)
    rawData = json.loads(r.text)
    if rawData['totalItems'] == 0:
        return {}
    else:
        return rawData

def searchGoogleBooksByKeywords(keyword_string, offset):
    url = 'https://www.googleapis.com/books/v1/volumes?q=' + keyword_string
    url += '&printType=books'
    url += '&startIndex=' + offset
    url += 'maxResults=20'
    payload = {'key':'AIzaSyAyR0m9gfSIuddjfY6nskanTg08X_62ICM'}
    r = requests.get(url,params=payload)
    rawData = json.loads(r.text)
    if rawData['totalItems'] == 0:
        return {}
    else:
        return rawData

#print getNewYorkTimesList('young-adult', 0)
