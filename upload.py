from firebase.setup import auth, db, storage, firestore
from firebase.article import upload_article
from firebase import schema
import os


def main():
    for filename in os.listdir('./article'):
        print(filename)
        


if __name__ == '__main__':
    main()
    
    
""" upload_article(
    schema.article(
        title='some title',
        body='some text',
        cover_image=
        'https://example.com/example.png'  # will be implemented later, this needs to be uploaded to the server as a file before article object is sent to database 
    )) """