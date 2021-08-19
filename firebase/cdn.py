import os
import time
import re
from sys import displayhook
from firebase_admin import credentials
from firebase_admin import auth
import firebase_admin
import pyrebase
from flask import *
from werkzeug.utils import secure_filename
from pyrebase import *

config = {
    # TODO: get config from firebase.setup.firebase_init()
    "foo": "bar"
}
path = os.getcwd()

UPLOAD_FOLDER = os.path.join(path, 'temporary')

if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__, template_folder='src')
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['FLASK_ENV'] = 'development'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
firebase = pyrebase.initialize_app(config)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


cred = credentials.Certificate('theistanbulchronicle-3173a-242f3f0f0efe.json')
auth = firebase.auth()
storage = firebase.storage()


class update_pp():
    def update(self):
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files.get('pfpinput', None)
        if file.filename == '':
            print('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print('File successfully uploaded')
            return redirect('/')
        else:
            print('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
