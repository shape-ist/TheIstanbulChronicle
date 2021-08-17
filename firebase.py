from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
from firebase_admin import initialize_app
import pyrebase
import re


def get_secrets():
    from dotenv import load_dotenv
    from os import getenv
    load_dotenv()

    GCP_PROJECT_ID = getenv('GCP_PROJECT_ID')
    SERVICE_ACCOUNT_FILE = getenv('SERVICE_ACCOUNT_FILE')
    STORAGE_BUCKET_NAME = getenv('STORAGE_BUCKET_NAME')
    return {
        'apiKey':             getenv('apiKey'),
        'authDomain':         getenv('authDomain'),
        'databaseURL':        getenv('databaseURL'),
        'projectId':          getenv('projectId'),
        'storageBucket':      getenv('storageBucket'),
        'messagingSenderId':  getenv('messagingSenderId'),
        'appId':              getenv('appId'),
        'measurementId':      getenv('measurementId')
    }


def firebase_init():
    # initialize firebase

    # get secrets from dotenv. see function get_secrets()
    firebaseConfig = get_secrets()
    firebase = pyrebase.initialize_app(firebaseConfig)
    cred = credentials.Certificate(
        'theistanbulchronicle-3173a-242f3f0f0efe.json')
    initialize_app(cred)
    auth = firebase.auth()
    db = firestore.client()
    return auth, db


class User():

    def __init__(self, email, password, display_name):
        # this method assumes that the passwords are not mismatched, please use js to check for matching password
        # (password matching was removed in pre-beta)
        auth.create_user_with_email_and_password(email, password)
        auth.sign_in_with_email_and_password(email, password)
        uid = auth.current_user['localId']

        # creates user document
        db.collection(u'users').document(uid).set({
            u'email':           email,
            u'bio':             '',
            u'uid':             uid,
            u'name':            display_name,
            u'pp':              '',
            u'elevation':       [],
            u'ban':             False
        })

    def __login__(self, email, password):
        auth.sign_in_with_email_and_password(email, password)


if __name__ == '__main__':
    auth, db = firebase_init()
