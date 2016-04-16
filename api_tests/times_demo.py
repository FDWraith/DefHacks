import requests
import json

#get list of all best seller lists
Listurl = 'http://api.nytimes.com/svc/books/v2/lists/names.json'
payload = {'api-key':'07dd07bcee660b08c3193b8876620845:13:75015836'}
fictionUrl = 'http://api.nytimes.com/svc/books/v2/lists/combined-print-and-e-book-fiction.json'
nonfictionUrl = 'http://api.nytimes.com/svc/books/v2/lists/combined-print-and-e-book-nonfiction.json'
r = requests.get(nonfictionUrl, params=payload)

print(r.url)
print(r.status_code)

fictionJson = json.loads(r.text)
print(fictionJson['results'][0]['book_details'][0]['title'])
