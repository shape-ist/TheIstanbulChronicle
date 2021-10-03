import pyrebase
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import initialize_app
from os import getenv
from dotenv import load_dotenv


def get_secrets():
    load_dotenv()

    GCP_PROJECT_ID = getenv('GCP_PROJECT_ID')
    SERVICE_ACCOUNT_FILE = getenv('SERVICE_ACCOUNT_FILE')
    STORAGE_BUCKET_NAME = getenv('STORAGE_BUCKET_NAME')
    return {
        'apiKey': getenv('apiKey'),
        'authDomain': getenv('authDomain'),
        'databaseURL': getenv('databaseURL'),
        'projectId': getenv('projectId'),
        'storageBucket': getenv('storageBucket'),
        'messagingSenderId': getenv('messagingSenderId'),
        'appId': getenv('appId'),
        'measurementId': getenv('measurementId')
    }


def firebase_init():
    # initialize firebase

    # get secrets from dotenv. see function get_secrets()
    firebaseConfig = get_secrets()
    firebase = pyrebase.initialize_app(firebaseConfig)
    cred = credentials.Certificate(getenv('certificate'))
    initialize_app(cred)
    auth = firebase.auth()
    db = firestore.client()
    storage = firebase.storage()
    return auth, db, storage, firestore


auth, db, storage, firestore = firebase_init()
# use 'from firebase.setup import auth' / 'from firestore.setup import storage' etc.
