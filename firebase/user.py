from firebase.setup import db, auth


def register(email, password, display_name):
    new_user = auth.create_user_with_email_and_password(email, password)
    uid = new_user['localId']

    # creates user document
    from firebase import schema
    db.collection(u'users').document(uid).set(
        schema.user(name=display_name, email=email, uid=uid))


def login(email, password):
    auth.sign_in_with_email_and_password(email, password)
    # TODO: implement persistent login here. (Maybe use @persistent decorator?)


def user_exists(uid):
    doc = db.collection('users').document(uid).get()
    return bool(doc.exists)


def delete_user(uid):
    db.collection(u'users').document(uid).delete()


def current():
    return auth.current_user


def current_uid():
    return auth.current_user['localId']


def is_signed_in():
    return current() is not None
