import Queue,access,json,requests,userdata,bookStorage,Book

def pToLoL(p):
    L = [];
    while(p.qsize() != 0):
        L.append(p.get());
    return L;

def LoLToP(L):
    p = Queue.PriorityQueue();
    for i in L:
        p.put(i);
    return p;

def initialize(p,username):
    addRandomBooks(p,username);
        
def swipeLeft(username, currentBook):
    isbn = currentBook.isbn;

    if isbn not in bookStorage.get():
        bookStorage.add(isbn, currentBook);
        
    userdata.addDislikedBook(username,isbn);
    for genre in isbn.subjects:
        temp = userdata.getTagList(username);
        if genre in temp:
            userdata.addTag(username,genre,temp[genre][0]+1);
        else:
            userdata.addTag(username,genre,1);

def swipeRight(username, currentBook):
    isbn = currentBook.isbn

    if isbn not in bookStorage.get():
        bookStorage.add(isbn,currentBook);
    
    userdata.addLikedBook(username,isbn);
    for genre in isbn.subjects:
        temp = userdata.getTagList(username);
        if genre in temp:
            userdata.addTag(username,genre,temp[genre][0]-1);
        else:
            userdata.addTag(username,genre,-1);
 
def saveBook(username, currentBook):
    isbn = currentBook.isbn;
    
    if isbn not in bookStorage.get():
        bookStorage.add(isbn,currentBook);

    userdata.addSavedBook(username,isbn);
        
    for genre in isbn.subjects:
        temp = userdata.getTagList(username);
        if genre in temp:
            userdata.addTag(username,genre,temp[genre][0]-3);
        else:
            userdata.addTag(username,genre,-3);

    temp = userdata.getTagList(username);
    for genre in temp:
        if temp[genre] >= 5:
            searchResults = search.search(genre);#seach returns a list of books of the genre param.
            for i in range(5):
                p.put( [ temp[genre]+3, searchResults[i] ] )
            userdata.addTag(username,genre,temp[genre][0]+3);

def addRandomBooks(p,username):
    list = access.getNewYorkTimesList('young-adult', str(userdata.getNum(username)) + '');
    userdata.changeNum(username, 20)
    for i in list:
        b = Book();
        list.fill_ny_times(b,i);
        isbn = i['isbn'];
        list.fill_open_library(b,access.getOpenLibraryBook(str(isbn)+''));
        p.put([0,b]);        

        
counter = 0;            
def display(username,p):    
    userdata.changeCurrentBook(username,p.get());
    currentBook = userdata.getCurrentBook(username);
    end = "";
    end += "<table>\n";
    if currentBook.title:
        end += "<tr><td><h1>Title: "+currentBook.title+"</h1></td></tr>\n";
    if currentBook.author:
        end += "<tr><td><h3>Author: "+currentBook.author+"</h3></td><tr>\n";
    end += "<tr><td><input class='btn btn-default' name='mode' type='submit' value ='left'</td>\n"
    if currentBook.cover_image:
        end += "<tr><td><img src='"+currentBook.cover_image+"'></td></tr>\n"    
    end += "<tr><td><h4>Basic Information:</h4></td></tr>\n";
    end += "<tr><td><ul>\n"
    if currentBook.main_category:
        end += "<li>Main Category: "+currentBook.main_category+"</li>\n";
    if currentBook.times_desc:
        end += "<li>Description: "+currentBook.times_desc+"</li>\n"; 
    if currentBook.google_desc:
        end += "<li>More: "+currentBook.google_desc+"</li>\n";
    if currentBook.page_count:
        end += "<li>Page Count: "+currentBook.page_count+"</li>\n";    
    if currentBook.language:
        end += "<li>Language: "+currentBook.language+"</li>\n";
    genres = '';
    if currentBook.subjects:
        for i in currentBook.subjects:
            genres += i +",";
    if currentBook.google_cats:
        for i in currentBook.subects:
            genres += i +",";
    genres= genres[:-1];
    if genres != '':
        end += "<li>Categories: "+genres+"</li>\n";
    end += "</ul></td></tr>\n";
    end += "<tr><td><input class='btn btn-default' name='mode' type='submit' value ='left'</td>"
    end += "<td><input class='btn btn-default' name='mode' type='submit' value ='left'</td>"
    end += "<td><input class='btn btn-default' name='mode' type='submit' value ='right'</td></tr>\n"
    #Algos
    if p.qsize() < 10:
        addRandomBooks(p,username)
    #if counter >= 5:
    #updatePriorityQueue()
    
    return end;
        
