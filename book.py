class Book(object):
    def __init__(self):
        #Common attributes
        self.title = ''
        self.author = ''
        self.publish_date = ''
        self.page_count = ''
        self.cover_image = ''
        self.isbn = ''
        #Open Library attributes
        self.open_url = ''
        self.genres = ''
        self.notes = ''
        #NY Times attributes
        self.times_desc = ''
        self.amazon_url = ''
        #Google Books attributes
        self.google_id = ''
        self.google_desc = ''
        self.main_category = ''
        self.google_cats = []
        self.google_rating = -1
        self.language = ''
        #User attributes
        self.user_saved = False
        self.save_date = -1

    def fill_open_library(self, open_info):
        if not self.title:
            self.title = open_info['title']
        if not self.author:
            self.author = open_info['author']
        if not self.publish_date:
            self.publish_date = open_info['publish_date']
        if not self.isbn:
            self.title = open_info['isbn']
        if not self.cover_image:
            self.cover_image = open_info['cover_image']
        if not self.page_count:
            self.title = open_info['page_count']
        self.open_url = open_info['url']
        self.genres = open_info['genres']
        self.notes = open_info['notes']

    def fill_ny_times(self, times_info):
        self.isbn = times_info['isbn']
        self.title = times_info['title']
        self.author = times_info['author']
        self.times_desc = times_info['description']
        self.amazon_url = times_info['url']

    def fill_google_books(self, google_info):
        self.google_id = google_info['id']
        if not self.title:
            self.title = google_info['title']
        if not self.author and 'authors' in google_info:
            joint_author = ''
            for a in google_info['volumeInfo']['title']:
                joint_author = joint_author + " and " + a
            self.author = joint_author
        if not self.publish_date and 'publishedDate' in google_info:
            self.publish_date = google_info['publishedDate']
        if not self.isbn and 'industryIdentifiers' in google_info:
            for identifier in google_info['industryIdentifiers']:
                if identifier['type'] == 'ISBN_10':
                    self.isbn = identifier['identifier']
        if not self.page_count and 'pageCount' in google_info:
            self.title = google_info['pageCount']
        if 'averageRating' in google_info:
            self.google_rating = google_info['averageRating']
        if 'language' in google_info:
            self.language = google_info['language']
        if 'mainCategory' in google_info:
            self.main_category = google_info['mainCategory']
        if 'categories' in google_info:
            self.google_cats = google_info['categories']
        if 'description' in google_info:
            self.google_desc = google_info['description']
        if not self.cover_image and 'imageLinks' in google_info:
            if 'large' in google_info['imageLinks']:
                self.cover_image = google_info['imageLinks']['large']
            elif 'extraLarge' in google_info['imageLinks']:
                self.cover_image = google_info['imageLinks']['extraLarge']
            elif 'medium' in google_info['imageLinks']:
                self.cover_image = google_info['imageLinks']['medium']

    def set_saved(self, value):
        user_saved = value

