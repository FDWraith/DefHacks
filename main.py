import Queue,access,json,requests,userdata

p = PriorityQueue();
num = 0;
currentBook = {};

def getCurrentBook():
    return currentBook;

def initialize():
    addRandomBooks();
        
def swipeLeft(username):
    isbn = currentBook.isbn;

    if !(isbn in bookStorage.getList()):
        bookStorage.add(isbn,currentBook);
        
    userdata.addDislikedBook(username,isbn);
    for genre in b.subjects:
        temp = getTag(username);
        if genre in temp:
            userdata.addTag(username,genre,temp[genre][0]+1);
        else:
            userdata.addTag(username,genre,1);

def swipeRight(username):
    isbn = currentBook.isbn

    if !(isbn in bookStorage.getList()):
        bookStorage.add(isbn,currentBook);
    
    userdata.addLikedBook(username,isbn);
    for genre in b.subjects:
        temp = getTag(username);
        if genre in temp:
            userdata.addTag(username,genre,temp[genre][0]-1);
        else:
            userdata.addTag(username,genre,-1);
 
def saveBook(username):
    isbn = currentBook.isbn;
    
    if !(isbn in bookStorage.getList()):
        bookStorage.add(isbn,currentBook);

    userdata.addSavedBook(username,isbn);
        
    for genre in b.subjects:
        temp = getTag(username);
        if genre in temp:
            userdata.addTag(username,genre,temp[genre][0]-3);
        else:
            userdata.addTag(username,genre,-3);

def updatePriorityQueue():
    temp = getTag(username);
    for genre in temp:
        if temp[genre] >= 5:
            searchResults = search.search(genre);#seach returns a list of books of the genre param.
            for i in range(5):
                p.put( [ temp[genre]+3, searchResults[i] ] )
            userdata.addTag(username,genre,temp[genre][0]+3);

def addRandomBooks():
    list = access.accessNewYorkTimesData('young-adult',num+'');
    num+=20;
    for i in list:
        b = Book();
        b.fill_ny_times(b,i);
        isbn = i['isbn'];
        b.fill_open_library(b,access.accessOpenLibraryData(isbn+''));
        p.put([0,b]);        

        
counter = 0;            
def display():    
    currentBook = p.get();
    end = "";
    end += "<table>\n";
    if currentBook.title:
        end += "<tr><td><h1>Title: "+currentBook.title+"</h1></td></tr>\n";
    if currentBook.author:
        end += "<tr><td><h3>Author: "+currentBook.autho+"</h3></td><tr>\n";
    if currentBook.cover_image:
        end += "<img src='"+currentBook.cover_image+"'>\n";
    end += "<tr><td><h4>Basic Information:</h4></td></tr>\n";
    end += "<tr><td><ul>\n"
    if currentBook.isbn:
        end += "<li>ISBN:"+currentBook.isbn+"</li>\n";
    if currentBook.page_count:
        end += "<li>Page Count"+currentBook.page_count+"</li>\n";
    if currentBook.page_count:
        end += "<li>"+currentBook.page_count+"</li>\n";
    if currentBook.page_count:
        end += "<li>"+currentBook.page_count+"</li>\n";
    if currentBook.page_count:
        end += "<li>"+currentBook.page_count+"</li>\n";
    if currentBook.page_count:
        end += "<li>"+currentBook.page_count+"</li>\n";
    if currentBook.page_count:
        end += "<li>"+currentBook.page_count+"</li>\n";
    if currentBook.page_count:
        end += "<li>"+currentBook.page_count+"</li>\n";
    if currentBook.page_count:
        end += "<li>"+currentBook.page_count+"</li>\n";
    if currentBook.page_count:
        end += "<li>"+currentBook.page_count+"</li>\n";
    if currentBook.page_count:
        end += "<li>"+currentBook.page_count+"</li>\n";
    if currentBook.page_count:
        end += "<li>"+currentBook.page_count+"</li>\n";
        
