#This file is a function
import json, requests

def accessData(isbn):
    url = "https://openlibrary.org/api/books?bibkeys=ISBN:{num}&format=json&jscmd=data".format(num = isbn);
    r = requests.get(url);
    rawData = json.loads(r.text);
    d = { };
    d['title'] = rawData["ISBN:{num}".format(num=isbn)]["title"];
    d['author'] = rawData["ISBN:{num}".format(num=isbn)]["authors"][0]["name"];
    d['publish_date'] = rawData["ISBN:{num}".format(num=isbn)]['publish_date'];
    d['url'] = rawData["ISBN:{num}".format(num=isbn)]['url'];
    d['page_count'] = rawData["ISBN:{num}".format(num=isbn)]['number_of_pages'];
    d['cover_image'] = rawData["ISBN:{num}".format(num=isbn)]['cover']['large'];
    genres = rawData['ISBN:{num}'.format(num=isbn)]['subjects'];
    #print(genres);
    for i in range(len(genres)):
       genres[i] = genres[i]['name'];
    d['genres'] = genres;
    d['notes'] = rawData["ISBN:{num}".format(num=isbn)]['notes'];

    return d;

#print(accessData('0451526538'))
