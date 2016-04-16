import requests
import json

searchUrl = 'https://www.googleapis.com/books/v1/volumes?q=harry_potter'
authKey = {'key':'AIzaSyAyR0m9gfSIuddjfY6nskanTg08X_62ICM'}

r = requests.get(searchUrl,params=authKey)

print(r.status_code)
print(r.text)