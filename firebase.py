from firebase_admin.auth import UserIdentifier
from flask import *
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
import pyrebase
from pyrebase import *
import base64
import re
from cryptography.fernet import Fernet


class User():
    def __init__(self, display_name, email):
        self.name = name
        self.age = age

    def __register__(self, email, password):
        if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        passwordrepeat = request.form.get("passwordagain")
        displayname = request.form.get("displayName")

        if password == passwordrepeat:
            auth.create_user_with_email_and_password(email, password)

            auth.sign_in_with_email_and_password(email, password)
            uid = auth.current_user['localId']
            print(uid)

            data = {
                u'bio': None,
                u'email': email,
                u'uid': uid,
                u'name': displayname,
                u'pfp': None,
            }

            db.collection(u'users').document(uid).set(data)

            encemail = f.encrypt(bytes(email, encoding="utf-8"))
            encpass = f.encrypt(bytes(password, encoding="utf-8"))

            resp = make_response()

            resp.set_cookie('email', encemail, max_age=None)

            resp.set_cookie('password', encpass, max_age=None)
            return resp

            @app.route("")
        elif password != passwordrepeat:
            raise Exception('PasswordMismatch')

    def __login__(self, email, passoword):
        auth.sign_in_with_email_and_password(email, password)

    # initialize firebase
firebaseConfig = {
    'apiKey': "AIzaSyD9_donSo5pL-y3BdqmSPooCkZvnBbwzmw",
    'authDomain': "theistanbulchronicle-3173a.firebaseapp.com",
    'databaseURL': "https://theistanbulchronicle-3173a-default-rtdb.europe-west1.firebasedatabase.app",
    'projectId': "theistanbulchronicle-3173a",
    'storageBucket': "theistanbulchronicle-3173a.appspot.com",
    'messagingSenderId': "987152272874",
    'appId': "1:987152272874:web:658d06259f17b2b94b3693",
    'measurementId': "G-8QS0MZ7BX0"
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
cred = credentials.Certificate('theistanbulchronicle-3173a-242f3f0f0efe.json')
firebase_admin.initialize_app(cred)
auth = firebase.auth()
db = firestore.client()

key = ((db.collection(u'encryption').document(
    u'eCWQsFFRnLqnybFoY6Sk')).get().to_dict())

f = Fernet(str.encode(key.get('token')))
