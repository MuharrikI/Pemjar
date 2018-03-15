import urllib.request, json

isbn = input("ISBN : ")

domain = "https://www.googleapis.com/books/v1/volumes?q=isbn:"

def get(ini_domain,ini_isbn):
    with urllib.request.urlopen(domain+str(isbn)) as google_url:
        data_json = json.loads(google_url.read().decode())

        for item in data_json['items']:
            print ("Judul Buku          : "+item['volumeInfo']['title'])
            print ("Pengarang Buku      : "+str(item['volumeInfo']['authors']))
            print ("Penerbit Buku       : "+item['volumeInfo']['publisher'])
            print ("Tanggal Terbit Buku : "+item['volumeInfo']['publishedDate'])

get(domain,isbn)

