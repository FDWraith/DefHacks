#This file is a function
import json, requests

def accessOpenLibraryData(isbn):
    #retunrs a dictionary of info on the book indicated by the isbn
    url = "https://openlibrary.org/api/books?bibkeys=ISBN:{num}&format=json&jscmd=data".format(num = isbn);
    r = requests.get(url);
    rawData = json.loads(r.text);
    if(rawData == { }):
        return { };
    d = { };
    d['isbn'] = isbn;
    d['title'] = rawData["ISBN:{num}".format(num=isbn)]["title"];
    d['author'] = rawData["ISBN:{num}".format(num=isbn)]["authors"][0]["name"];
    d['publish_date'] = rawData["ISBN:{num}".format(num=isbn)]['publish_date'];
    d['url'] = rawData["ISBN:{num}".format(num=isbn)]['url'];
    d['page_count'] = rawData["ISBN:{num}".format(num=isbn)]['number_of_pages'];
    d['cover_image'] = rawData["ISBN:{num}".format(num=isbn)]['cover']['large'];
    genres = rawData['ISBN:{num}'.format(num=isbn)]['subjects'];
    #print(genres);
    for i in range(len(genres)):
       genres[i] = genres[i]['name'].lower();
    d['genres'] = genres;
    d['notes'] = rawData["ISBN:{num}".format(num=isbn)]['notes'];

    return d;

def accessNewYorkTimesData(listname,offset):
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

def accessGoogleBooksData(volume_id):
    url = 'https://www.googleapis.com/books/v1/volumes/' + volume_id
    payload = {'key':'AIzaSyAyR0m9gfSIuddjfY6nskanTg08X_62ICM'}
    r = requests.get(url,params=payload)
    rawData = json.loads(r.text)
    return rawData

#print accessGoogleBooksData("zyTCAlFPjgYC")

#print accessNewYorkTimesData('combined-print-and-e-book-fiction','0');

