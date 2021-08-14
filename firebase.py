import os
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
from firebase_admin import initialize_app
import pyrebase
import re


def firebase_init():
    # initialize firebase
    firebaseConfig = {
        'apiKey': "             AIzaSyD9_donSo5pL-y3BdqmSPooCkZvnBbwzmw",
        'authDomain':           "theistanbulchronicle-3173a.firebaseapp.com",
        'databaseURL':          "https://theistanbulchronicle-3173a-default-rtdb.europe-west1.firebasedatabase.app",
        'projectId':            "theistanbulchronicle-3173a",
        'storageBucket':        "theistanbulchronicle-3173a.appspot.com",
        'messagingSenderId':    "987152272874",
        'appId':                "1:987152272874:web:658d06259f17b2b94b3693",
        'measurementId':        "G-8QS0MZ7BX0"
    }
    firebase = initialize_app(firebaseConfig)
    cred = credentials.Certificate(
        'theistanbulchronicle-3173a-242f3f0f0efe.json')
    pyrebase.initialize_app(cred)
    auth = firebase.auth()
    db = firestore.client()
    return auth, db


class User():

    def __init__(self, email, password, display_name):
        # this method assumes that the passwords are not mismatched, please use js to check for matching password
        auth.create_user_with_email_and_password(email, password)
        auth.sign_in_with_email_and_password(email, password)
        uid = auth.current_user['localId']

        db.collection(u'users').document(uid).set({
            u'email':           email,
            u'bio':             '',
            u'uid':             uid,
            u'name':            display_name,
            u'pp':              '',
            u'elevation':       [],
            u'ban':             False
        })

    def __login__(self, email, passoword):
        auth.sign_in_with_email_and_password(email, password)


if __name__ == '__main__':
    auth, db = firebase_init()
    User("binandioglu2006@gmail.com", "31", "Barış İnandıoğlu")
