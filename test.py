import urllib.request
import json
import sys

with urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=isbn:"+sys.argv[1]+"&key=AIzaSyCj_OnaX6xkDIlo4jVY7WbrM0TGZjwWu70") as url:
    data=json.loads(url.read().decode())

    for item in data['items']:
        print ("Judul           : "+item['volumeInfo']['title'])
        print ("Pengarang       : "+str(item['volumeInfo']['authors']))
        print ("Penerbit        : "+item['volumeInfo']['publisher'])
        print ("Tannggal Terbit : "+item['volumeInfo']['publishedDate'])



