#This module contains a method that returns a book related to a keyword
#Implements userdata, access, book
import book, access, userdata

#takes search_term (subject or goog_cat), type (google or open), and username
#returns book or None if no relevant books found
def getRelatedBook(search_term, type, username):
    if type == 'google':
        result_dict = access.searchGoogleBooksByCategory(search_term)
    elif type == 'open':
        result_dict  = access.searchGoogleBooksByKeywords(search_term)
    if result_dict == {}:
        return None
    viewed_isbns = userdata.getLikedBookList(username)
    viewed_isbns.extend(userdata.getDislikedBookList(username))
    found_books = result_dict['items']
    for book_dict in found_books:
        isbn = ''
        for identifier in book_dict['industryIdentifiers']:
            if identifier['type'] == 'ISBN_10':
                isbn = identifier['identifier']
        if isbn != '' and (isbn not in viewed_isbns):
            ret_book = book.Book()
            ret_book.fill_google_books(book_dict)
            ret_book.fill_open_library(ret_book.isbn)
            return ret_book
    return None

#gets best unseen book from new york times list, or None if none high enough found
#takes username
def getBestNewYorkTimesBook(username):
    times_offset = userdata.getNum(username)
    book_list = access.getNewYorkTimesList(times_offset)
    viewed_isbns = userdata.getLikedBookList(username)
    viewed_isbns.extend(userdata.getDislikedBookList(username))
    for book_dict in book_list:
        if book_dict['isbn'] not in viewed_isbns:
            ret_book = book.Book()
            fillFromAllSources(ret_book, book_dict['isbn'])
            return ret_book
    #Make sure this is consistent with userdata api
    userdata.changeNum(username, 20)
    return None

#Fills book with data pulled from all sources
def fillFromAllSources(mod_book, isbn):
    mod_book.fill_open_library(access.getOpenLibraryBook(isbn))
    mod_book.fill_google_books(access.getGoogleBookByISBN(isbn))