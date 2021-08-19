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
    """
    issue:
    
        requests.exceptions.HTTPError: [Errno 400 Client Error: Bad Request for url: https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyD9_donSo5pL-y3BdqmSPooCkZvnBbwzmw] {
        "error": {
        "code": 400,
        "message": "EMAIL_NOT_FOUND",
        "errors": [
        {
        "message": "EMAIL_NOT_FOUND",
        "domain": "global",
        "reason": "invalid"
        }
        ]
        }
        }
    """
