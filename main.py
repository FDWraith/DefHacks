import Queue,access,json,requests,userdata

p = PriorityQueue();
userData = { [ ],#List of saved books
             [ ],#List of liked books
             [ ],#List of disliked books
             { } }#Dictionary of tags with ranking
           #TEMP, will replace with accessor method later

def initialize():
    list = access.accessNewYorkTimesData('','0');
    for i in list:
        b = Book();
        b.fill_ny_times(b,i);
        isbn = i['isbn'];
        b.fill_open_library(b,access.accessOpenLibraryData(isbn+''));
        
        p.put([0,b]);        
        
def swipeLeft(b):
    userdata.addDislikedBook(username,b);
    for genre in b.genres:
        temp = getTag(username);
        if genre in temp:
            userdata.addTag(username,genre,temp[genre]+1);
        else:
            userdata.addTag(username,genre,1);

def swipeRight(b):
    userdata.addLikedBook(username,b);
    for genre in b.genres:
        temp = getTag(username);
        if genre in temp:
            userdata.addTag(username,genre,temp[genre]-1);
        else:
            userdata.addTag(username,genre,-1);
 
def saveBook(b):
    userdata.addSavedBook(username,b);
    for genre in b.genres:
        temp = getTag(username);
        if genre in temp:
            userdata.addTag(username,genre,temp[genre]-3);
        else:
            userdata.addTag(username,genre,-3);

def updatePriorityQueue():
    temp = getTag(username);
    for genre in temp:
        if temp[genre] >= 5:
            searchResults = search.search(genre);#seach returns a list of books of the genre param.
            for i in range(5):
                p.put( [ temp[genre]+3, searchResults[i] ] )
            userdata.addTag(username,genre,temp[genre]+3);


            
            
