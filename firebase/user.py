from firebase.setup import db, auth


def register(email, password, display_name):
    auth.create_user_with_email_and_password(email, password)
    login(email, password)
    uid = auth.current_user['localId']

    # creates user document
    from firebase import schema
    db.collection(u'users').document(uid).set(
        schema.user(name=display_name, email=email, uid=uid))

    # this function expects you to explicitly sign the user in after registration


def login(email, password):
    auth.sign_in_with_email_and_password(email, password)
    # TODO: implement persistent login here. (Maybe use @persistent decorator?)


def user_exists(uid):
    doc = db.collection('users').document(uid).get()
    return bool(doc.exists)


def delete_user(uid):
    db.collection(u'users').document(uid).delete()


def is_signed_in():
    return 0 if auth.current_user is None else 1