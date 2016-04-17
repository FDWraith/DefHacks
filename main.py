import Queue,access,json,requests,userdata,bookStorage,book,bookutils

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

def toBook(book_isbn):
    b = book.Book();
    bookutils.fillFromAllSources(b,book_isbn)
    return b

def toISBN(b):
    return b['isbn']


def initialize(p,username):
    addRandomBooks(p,username);
        
def swipeLeft(username, currentBook):
    isbn = currentBook.isbn;
    if isbn not in bookStorage.getJson():
        bookStorage.add(isbn, currentBook);
    userdata.addDislikedBook(username,isbn);
    for genre in currentBook.subjects:
        tempTagDict = userdata.getTagDict(username);
        if genre in tempTagDict:
            userdata.addTag(username,genre,tempTagDict[genre][0]+1);
        else:
            userdata.addTag(username,genre,1);

def swipeRight(username, currentBook):
    isbn = currentBook.isbn;
    if isbn not in bookStorage.getJson():
        bookStorage.add(isbn, currentBook);
    userdata.addLikedBook(username,isbn);
    for genre in currentBook.subjects:
        tempTagDict = userdata.getTagDict(username);
        if genre in tempTagDict:
            userdata.addTag(username,genre,tempTagDict[genre][0]-1);
        else:
            userdata.addTag(username,genre,-1);
 
def saveBook(username, currentBook, p):
    isbn = currentBook.isbn;
    
    if isbn not in bookStorage.getJson():
        bookStorage.add(isbn,currentBook);

    userdata.addSavedBook(username,isbn);
        
    for genre in isbn.subjects:
        temp = userdata.getTagDict(username);
        if genre in temp:
            userdata.addTag(username,genre,temp[genre][0]-3);
        else:
            userdata.addTag(username,genre,-3);

    temp = userdata.getTagDict(username);
    """
    for genre in temp:
        if temp[genre] >= 5:
            searchResults = search.search(genre);#seach returns a list of books of the genre param.
            for i in range(5):
                p.put( [ temp[genre]+3, searchResults[i] ] )
            userdata.addTag(username,genre,temp[genre][0]+3);
            """

def updateBookQueue(username, book_queue):
    ranked_tags = userdata.getTagDict()
    if book_queue.qsize() < 10:
        #ASSUME TYPE OPEN
        popTag = userdata.getPopularTag(username)
        if popTag != None:
            relatedBook = bookutils.getRelatedBook(popTag, 'open', username)
            if relatedBook != None:
                book_queue.put([1, relatedBook])
                #Update tags after swiping
            else:
                #Here is where I'll try to get a new times book until the list runs out
                #Techically this will be an infinite loop, but whatever, we wont reach it in demo
                nextTimesBook = None
                while nextTimesBook == None:
                    nextTimesBook = bookutils.getBestNewYorkTimesBook(username)
                book_queue.put([0, nextTimesBook])


def addRandomBooks(p,username):
    list = access.getNewYorkTimesList('young-adult', str(userdata.getNum(username)) + '');
    userdata.changeNum(username, 20)
    for i in list:
        b = book.Book();
        b.fill_ny_times(i);
        isbn = i['isbn'];
        bookutils.fillFromAllSources(b, isbn)
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
        
